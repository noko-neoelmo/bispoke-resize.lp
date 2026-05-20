"""
Switch LP campaign: LINE開設記念15%OFF -> 2つ以上で10%OFF (まとめ割)
Target: resize/index.html
"""

import re
from pathlib import Path

HTML = Path("resize/index.html")
content = HTML.read_text(encoding="utf-8")
original = content

# ── 1. Hero promo band ──
content = content.replace(
    '<span class="hero-v2-promo-flag">LINE開設記念</span>',
    '<span class="hero-v2-promo-flag">まとめ割</span>',
)
content = content.replace(
    """<span class="hero-v2-promo-prices">
                    <span class="hero-v2-promo-old">¥11,000<span class="yen-sub">〜</span></span>
                    <span class="hero-v2-promo-arrow" aria-hidden="true">→</span>
                    <strong class="hero-v2-promo-new">¥9,350<span class="yen-sub">〜</span></strong>
                </span>
                <span class="hero-v2-promo-pct">15%OFF</span>
                <span class="hero-v2-promo-deadline">5/31まで</span>""",
    """<span class="hero-v2-promo-prices">
                    <strong class="hero-v2-promo-new">2つ以上のサイズ直しで</strong>
                </span>
                <span class="hero-v2-promo-pct">10%OFF</span>""",
)

# ── 2. Pricing promo callout ──
content = content.replace(
    '<span class="promo-callout-tag">LINE OPEN COMMEMORATION</span>',
    '<span class="promo-callout-tag">BUNDLE DISCOUNT</span>',
)
content = content.replace(
    '公式LINE開設を記念して、お見積もり<span class="promo-callout-pct">15</span>%OFF。',
    '2つ以上の指輪サイズ直しで<span class="promo-callout-pct">10</span>%OFF。',
)

# Pricing grid: 15%OFF prices -> 10%OFF prices
replacements_prices = [
    ("&yen;9,350",  "&yen;9,900"),
    ("&yen;12,750", "&yen;13,500"),
    ("&yen;21,250", "&yen;22,500"),
]
for old, new in replacements_prices:
    content = content.replace(old, new)

# Promo deadline
content = content.replace(
    '対象：<strong>2026年5月31日まで</strong>にLINEでお見積もり依頼をいただいた方',
    '対象：<strong>2つ以上の指輪</strong>を同時にご依頼いただいた方',
)

# ── 3. CTA button text (after pricing) ──
content = content.replace(
    'LINEで15%OFF即日お見積もり',
    'LINEで無料お見積もり',
)
content = content.replace(
    '公式LINE開設記念｜5/31まで限定',
    'まとめ割｜2つ以上で10%OFF',
)

# ── 4. FAQ 料金回答 ──
content = content.replace(
    '<strong>※2026年5月31日まで、公式LINE開設記念としてお見積りから15%オフでお仕立ていたします。</strong>',
    '<strong>※2つ以上の指輪を同時にご依頼いただくと、10%OFFでお仕立ていたします。</strong>',
)

# ── 5. Price note (※公式LINE開設記念15%OFF...) ──
content = content.replace(
    '※公式LINE開設記念15%OFFは、2026年5月31日までにLINEでお見積もり依頼をいただいた方が対象です。他キャンペーンとの併用はできません。',
    '※まとめ割10%OFFは、2つ以上の指輪サイズ直しを同時にご依頼いただいた場合に適用されます。他キャンペーンとの併用はできません。',
)

# ── 6. JSON-LD FAQ ──
content = content.replace(
    'お見積もりは無料ですので、LINEでお気軽にご相談ください。"',
    'お見積もりは無料ですので、LINEでお気軽にご相談ください。2つ以上の指輪を同時にご依頼いただくと10%OFFになります。"',
)

# ── 7. Header CTA ──
content = content.replace(
    '15%OFFで見積',
    'まとめ割で見積',
)

# ── 8. Promo banner ──
content = content.replace(
    '<span class="promo-banner-deadline">5/31まで！</span>\n        <span class="promo-banner-text">LINE開設記念｜お見積りから<span class="promo-banner-strong">15%OFF</span></span>',
    '<span class="promo-banner-text">まとめ割｜2つ以上のサイズ直しで<span class="promo-banner-strong">10%OFF</span></span>',
)

# ── 9. Floating CTA ──
content = content.replace(
    'LINE開設記念！お見積りから15%OFF',
    'まとめ割！2つ以上で10%OFF',
)

# ── 10. <title> tag ──
content = content.replace(
    '【LINE開設記念15%OFF】',
    '【まとめ割10%OFF】',
)

# ── 11. meta description ──
content = content.replace(
    '【公式LINE開設記念｜お見積りから15%オフ・5/31まで】',
    '【まとめ割｜2つ以上のサイズ直しで10%OFF】',
)

# ── Verify changes were made ──
if content == original:
    print("ERROR: No changes were made. The source may have already been updated.")
    exit(1)

changes = sum(1 for a, b in zip(original, content) if a != b)
HTML.write_text(content, encoding="utf-8")
print(f"Campaign switched successfully. ({changes} character diffs)")
