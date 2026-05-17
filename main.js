// ── Mobile Nav Toggle ──────────────────────────────────
const toggle = document.getElementById('navToggle');
const links  = document.getElementById('navLinks');
if (toggle && links) {
  toggle.addEventListener('click', () => {
    links.classList.toggle('open');
  });
}

// ── Gallery Filter Buttons (visual only) ──────────────
document.querySelectorAll('.filter-btn').forEach(btn => {
  btn.addEventListener('click', () => {
    document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
  });
});

// ── Password Strength Meter ────────────────────────────
const pwInput = document.getElementById('password');
const pwBar   = document.getElementById('strengthFill');
if (pwInput && pwBar) {
  pwInput.addEventListener('input', () => {
    const v = pwInput.value;
    let pct = 0, color = '#f96167';
    if (v.length >= 6)  { pct = 40; color = '#f96167'; }
    if (v.length >= 8)  { pct = 65; color = '#f0a040'; }
    if (v.length >= 10 && /[A-Z]/.test(v) && /[0-9]/.test(v)) { pct = 100; color = '#27ae60'; }
    pwBar.style.width    = pct + '%';
    pwBar.style.background = color;
  });
}

// ── Auto-dismiss flash messages ────────────────────────
setTimeout(() => {
  document.querySelectorAll('.flash').forEach(el => {
    el.style.opacity = '0';
    el.style.transition = 'opacity .4s';
    setTimeout(() => el.remove(), 400);
  });
}, 5000);
