# bispoke-resize.lp

RETOLD TOKYO サイズ直しLP（静的HTML）。本番: https://retold.tokyo/resize

## 構成

- `resize/index.html` — LP本体（単一HTML、CSS/JSインライン、約3200行）
- `resize/images/` — 画像アセット
- `resize/preview.html` — プレビュー版
- `vercel.json` — Vercelリライト設定（/resize/application/* → retold-resize-app.vercel.app）
- `.github/workflows/` — キャンペーン自動切替ワークフロー
- `.github/scripts/` — 切替用Pythonスクリプト

## デプロイ

mainにpush → Vercel自動デプロイ。PRは不要（静的HTML単体のため）。

## LP セクション構成（index.html）

1. Header（固定、LINE CTAボタン）
2. Promo Banner（キャンペーン告知帯）
3. Hero（FV: 価格・バッジ・CTA）
4. YOUR CONCERN（悩み4項目）→ Our Pride（職人紹介・事例）
5. Founder（創業者の思い）
6. PRICING（料金表・プロモ・対応素材一覧）`#price`
7. PROCESS（仕立ての流れ3ステップ）`#process`
8. FAQ（10問）`#faq`
9. Footer
10. Floating CTA（スクロール追従）

## キャンペーン切替

### 現行: LINE開設記念15%OFF（〜5/31）
### 次回: まとめ割10%OFF（5/26 00:00 JST自動切替）

- ワークフロー: `.github/workflows/campaign-switch-20260526.yml`
- スクリプト: `.github/scripts/switch-campaign-bundle-discount.py`
- 監視: RemoteTrigger `trig_01ShQ16TGiqHrJZ2QMKT4rax`（5/26 01:17 JST）
- 変更箇所11箇所: title, meta, ヘッダーCTA, プロモバナー, ヒーロー帯, 料金callout, 料金grid, 料金CTA, FAQ, 注釈, フローティングCTA

キャンペーン切替時は `switch-campaign-bundle-discount.py` を参考に、同様のスクリプト+ワークフローで自動化する。

## 広告運用メモ

- Google Ads: サイズ直しキャンペーン（1広告グループ「サイズ直し」）
- CPA目標: ¥4,600（現状）→ ¥3,000以下を目指す
- 高CVRワード: 地域名+サイズ直し、大きく/小さく+料金
- /resize#price 着地のCTRが通常の3.4倍 → 料金系KWは#price着地推奨
- Meta: リターゲティング設定済み（2026-05-20）
- 除外KW: 買取系・競合店名・購入系は除外済み

## 編集時の注意

- CSSはすべてインライン（`<style>`タグ内）。外部CSSファイルなし
- 画像はすべて `/resize/images/` 以下。**WebP配信（2026-06-05〜）**: 参照は `.webp`、PNG/JPG原本も残置。新規画像は `node ~/Projects/retold-tokyo/scripts/optimize-images.mjs resize/images --quality=72 --max-width=1100` でWebP化し、`src`/`url()` は `.webp` を参照すること（JSON-LDの `"image"` はpng維持）。FVヒーロー(CSS背景)は `<link rel=preload as=image fetchpriority=high>` 済み
- CTA href はすべて `https://liff.line.me/2009801854-l9LrHK08/`
- `data-cta` 属性でGTM dataLayerイベント `line_cta_click` を発火
- 料金変更時はFAQ・JSON-LD・meta description・プロモバナー・フローティングCTAも忘れず更新

## デザインシステム（DESIGN.md）

このLPの配色・タイポ・CTA・トーンは RETOLD TOKYO デザインシステムに従う。トークンの正本は [`./DESIGN.md`](./DESIGN.md)（[Google Labs DESIGN.md フォーマット](https://github.com/google-labs-code/design.md)準拠、`bispoke-cxo` がマスター）。

- インラインCSSの色は DESIGN.md の `colors`（CTA=Navy `#1B2A4A`、背景=Off White `#FAF8F5`、テキスト=Ink `#3D3D3D` 等）に一致させる
- セリフ体・グラデーション・キラキラ・暖色演出は禁止（DESIGN.md「Do's and Don'ts」参照）
- 正本: https://github.com/noko-neoelmo/bispoke-cxo/blob/main/DESIGN.md
