import sys, io, subprocess
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

path = 'index.html'
content = open(path, encoding='utf-8').read()

MERCH_URL = 'https://shop.areswear.com/org/ringoes-rampagers-shop'

# ── 1. Add Merch to nav ───────────────────────────────────────────────
old_nav = '''    <li><a href="#connect">Connect</a></li>
    <li><a href="#join">Join Us</a></li>'''
new_nav = '''    <li><a href="#connect">Connect</a></li>
    <li><a href="''' + MERCH_URL + '''" target="_blank">Merch</a></li>
    <li><a href="#join">Join Us</a></li>'''

if old_nav in content:
    content = content.replace(old_nav, new_nav)
    print("✅ Added Merch to nav")
else:
    print("❌ Could not find nav insertion point")

# ── 2. Add Merch card in Connect section (primary cards row) ──────────
# Add it as a primary link-card alongside WhatsApp and Facebook
old_connect_primary_end = '''    <!-- EDIT FACEBOOK LINK BELOW -->
    <a class="link-card" href="https://www.facebook.com/groups/1389121398590076" target="_blank">
      <div class="primary-badge">Primary</div>
      <span class="link-icon">&#128216;</span>
      <span class="link-label">Facebook Group</span>
      <span class="link-sub">Photos, event announcements, and community discussion.</span>
    </a>
  </div>'''

new_connect_primary_end = '''    <!-- EDIT FACEBOOK LINK BELOW -->
    <a class="link-card" href="https://www.facebook.com/groups/1389121398590076" target="_blank">
      <div class="primary-badge">Primary</div>
      <span class="link-icon">&#128216;</span>
      <span class="link-label">Facebook Group</span>
      <span class="link-sub">Photos, event announcements, and community discussion.</span>
    </a>
    <a class="link-card" href="''' + MERCH_URL + '''" target="_blank">
      <div class="primary-badge" style="background:#e6f8f5;color:#0a8f7c;">Shop</div>
      <span class="link-icon">&#128085;</span>
      <span class="link-label">Merch Store</span>
      <span class="link-sub">Official Ringoes Rampagers gear — shirts, hats, and more!</span>
    </a>
  </div>'''

if old_connect_primary_end in content:
    content = content.replace(old_connect_primary_end, new_connect_primary_end)
    print("✅ Added Merch card to Connect section")
else:
    print("❌ Could not find Connect primary cards end")

open(path, 'w', encoding='utf-8').write(content)
print(f"✅ Saved ({len(content.splitlines())} lines)")

# ── verify ────────────────────────────────────────────────────────────
c = open(path, encoding='utf-8').read()
checks = {
    "Merch URL in nav":        MERCH_URL in c and 'Merch</a>' in c,
    "Merch card in Connect":   'Merch Store' in c,
    "Merch link opens new tab": 'target="_blank"' in c,
    "Nav still has all links": all(x in c for x in ['href="#runs"','href="#races"','href="#photos"','href="#connect"','href="#join"']),
}
print("\n=== Checks ===")
for k, v in checks.items():
    print(f"  {'✅' if v else '❌'} {k}")

# ── commit & push ─────────────────────────────────────────────────────
r1 = subprocess.run(['git','add','-A'], capture_output=True, text=True, cwd=r'C:\temp\ringoesrampagers')
r2 = subprocess.run(['git','commit','-m','Add merch store link to nav and Connect section'], capture_output=True, text=True, cwd=r'C:\temp\ringoesrampagers')
print("\ncommit:", r2.stdout.strip())
r3 = subprocess.run(['git','push','origin','main'], capture_output=True, text=True, cwd=r'C:\temp\ringoesrampagers')
print("push:", r3.stdout.strip() or r3.stderr.strip())
print("code:", r3.returncode)
