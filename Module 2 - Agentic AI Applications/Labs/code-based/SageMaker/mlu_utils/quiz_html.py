"""
Comm-free quiz implementation.

Root cause (evidenced this session):
- Environment runs `jupyter_server_documents` (0.2.5) as the comm/document
  backend. ipywidgets rely on comm channels bound by the frontend widget
  manager. This backend has a per-view binding reliability problem: each
  top-level widget view has an independent probability of failing to bind
  ("Error displaying widget: model not found").
- Observed behavior confirms this: adding delay does NOT help (so it is not a
  timing race), but REDUCING the number of top-level widget views reduces the
  failures proportionally (so failures scale with number of views).

Fix: render the quiz as self-contained HTML + inline JavaScript. This uses NO
ipywidgets and NO comm channels, so there is no widget-manager binding step to
fail. It cannot hit the model-not-found bug regardless of the comm backend.

State (selection, submitted) lives in the browser DOM/JS, exactly like the
ipywidgets version lived in Python — no kernel round-trip is needed for a
self-check quiz.
"""

import json
import uuid
from IPython.display import HTML, display


class HtmlQuiz:
    def __init__(self, question):
        self.question_text = question["question"]
        self.options = question["options"]
        self.correct_index = question["correctIndex"]

    def _html(self):
        qid = "quiz_" + uuid.uuid4().hex[:10]
        options_json = json.dumps(self.options)
        options_buttons = "".join(
            f'<button type="button" class="qopt" data-idx="{i}" '
            f'onclick="{qid}_select({i})">{self._esc(opt)}</button>'
            for i, opt in enumerate(self.options)
        )
        return f"""
<div id="{qid}" style="max-width:700px;border:1px solid #dee2e6;border-radius:10px;
     padding:20px;margin:15px 0;box-shadow:0 2px 10px rgba(0,0,0,0.1);
     font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;">
  <div style="font-size:18px;font-weight:500;color:#2c3e50;margin-bottom:20px;
       padding:15px;background:#f8f9fa;border-left:4px solid #3498db;
       border-radius:4px;">{self._esc(self.question_text)}</div>
  <div id="{qid}_opts" style="display:flex;flex-direction:column;">
     {options_buttons}
  </div>
  <div style="margin-top:15px;">
    <button type="button" id="{qid}_submit" disabled
       onclick="{qid}_submit_fn()"
       style="padding:8px 16px;border:none;border-radius:5px;background:#3498db;
       color:#fff;font-weight:bold;cursor:pointer;opacity:0.5;">Submit Answer</button>
    <button type="button" id="{qid}_reset" onclick="{qid}_reset_fn()"
       style="display:none;padding:8px 16px;border:none;border-radius:5px;
       background:#f0ad4e;color:#fff;font-weight:bold;cursor:pointer;
       margin-left:10px;">Try Again</button>
  </div>
  <div id="{qid}_feedback" style="margin-top:15px;"></div>
</div>
<style>
  #{qid} .qopt {{
     text-align:left;white-space:normal;word-wrap:break-word;
     font-weight:normal;min-height:40px;line-height:1.5;width:100%;
     padding:12px 15px;margin:8px 0;border:2px solid #e9ecef;border-radius:8px;
     background:#fff;color:#212529;cursor:pointer;transition:all 0.2s ease;
  }}
  #{qid} .qopt:hover {{ transform:translateY(-2px);
     box-shadow:0 4px 8px rgba(0,0,0,0.1); }}
  #{qid} .qopt.selected {{ background:#e8f4fc;color:#0056b3;
     border:2px solid #3498db; }}
  #{qid} .qopt.correct {{ background:#d4edda;color:#155724; }}
  #{qid} .qopt.incorrect {{ background:#f8d7da;color:#721c24; }}
</style>
<script>
(function() {{
  var selected = -1;
  var correctIndex = {self.correct_index};
  var options = {options_json};
  window["{qid}_select"] = function(i) {{
    selected = i;
    var opts = document.querySelectorAll("#{qid} .qopt");
    opts.forEach(function(b, j) {{
      b.className = "qopt" + (j === i ? " selected" : "");
    }});
    var sb = document.getElementById("{qid}_submit");
    sb.disabled = false; sb.style.opacity = "1";
  }};
  window["{qid}_submit_fn"] = function() {{
    if (selected < 0) return;
    var opts = document.querySelectorAll("#{qid} .qopt");
    var fb = document.getElementById("{qid}_feedback");
    if (selected === correctIndex) {{
      opts[selected].className = "qopt correct";
      fb.innerHTML = '<div style="padding:12px 15px;background:#d4edda;'
        + 'color:#155724;border-radius:5px;font-weight:bold;">'
        + '&#10003; Correct! Well done!</div>';
    }} else {{
      opts[selected].className = "qopt incorrect";
      fb.innerHTML = '<div style="padding:12px 15px;background:#f8d7da;'
        + 'color:#721c24;border-radius:5px;font-weight:bold;">'
        + '&#10007; Incorrect. Try again.</div>';
    }}
    opts.forEach(function(b) {{ b.disabled = true; b.style.cursor = "default"; }});
    var sb = document.getElementById("{qid}_submit");
    sb.disabled = true; sb.style.opacity = "0.5";
    document.getElementById("{qid}_reset").style.display = "inline-block";
  }};
  window["{qid}_reset_fn"] = function() {{
    selected = -1;
    var opts = document.querySelectorAll("#{qid} .qopt");
    opts.forEach(function(b) {{
      b.className = "qopt"; b.disabled = false; b.style.cursor = "pointer";
    }});
    document.getElementById("{qid}_feedback").innerHTML = "";
    var sb = document.getElementById("{qid}_submit");
    sb.disabled = true; sb.style.opacity = "0.5";
    document.getElementById("{qid}_reset").style.display = "none";
  }};
}})();
</script>
"""

    @staticmethod
    def _esc(s):
        return (str(s).replace("&", "&amp;").replace("<", "&lt;")
                .replace(">", "&gt;"))

    def display(self):
        display(HTML(self._html()))
