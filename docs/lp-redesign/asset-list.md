# LPリデザイン用アセット配置ガイド

以下の画像をリポジトリへ配置してください。

## 配置先

```txt
public/images/resize-lp/
```

## ファイル一覧

### 1. current-hero-reference.webp

用途：

- 現在のLPヒーローの比較用
- Claude Codeが改善前後を比較するため

ファイル名：

```txt
current-hero-reference.webp
```

### 2. target-mobile-hero-reference.webp

用途：

- 目標デザイン参照
- スマホ最適レイアウトの再現用

ファイル名：

```txt
target-mobile-hero-reference.webp
```

## 最終構成

```txt
public/
  images/
    resize-lp/
      current-hero-reference.webp
      target-mobile-hero-reference.webp
```

## 補足

- WebP推奨
- 画像は比較参照用なので、実装時にそのまま使わなくてもよい
- ただし余白設計、CTA位置、リングゲージカード配置、情報優先度は参考にする

## 実装で重要なポイント

- 0.5号刻みを最上位訴求にする
- LINE CTAをファーストビュー内に入れる
- 他店で断られた指輪訴求を強める
- ホワイトベース＋ネイビーで上品にする
- 買取店・修理屋・チラシ感を減らす
