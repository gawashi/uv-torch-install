# uv-torch-install

uvを使用してPyTorchをインストールするプロジェクトです。

## 概要

このプロジェクトでは、Astral社の依存関係管理ツール `uv` を使用してPyTorchを適切にインストールし、CUDA対応の環境でテストを行います。

## インストール手順

### 1. プロジェクトのセットアップ

```bash
# 依存関係のインストール
uv add torch torchvision
```

### 2. インストール内容

uvによって以下のパッケージが自動的にインストールされます：

- **PyTorch 2.8.0** (CUDA 12.8対応版)
- **Torchvision 0.23.0** (CUDA 12.8対応版)
- **NVIDIA CUDA ライブラリ群**:
  - nvidia-cublas-cu12
  - nvidia-cudnn-cu12
  - nvidia-cufft-cu12
  - nvidia-curand-cu12
  - nvidia-cusolver-cu12
  - nvidia-cusparse-cu12
  - その他のCUDAサポートライブラリ
- **その他の依存関係**: numpy, sympy, triton等

## 実行方法

```bash
# PyTorchの動作テスト
uv run python main.py
```

## 期待される出力

```
Hello from uv-torch-install!
PyTorch version: 2.8.0+cu128
Torchvision version: 0.23.0+cu128
CUDA available: True
CUDA version: 12.8
Number of CUDA devices: 1
Current CUDA device: 0
Device name: NVIDIA GeForce RTX 3090

Random tensor:
tensor([[ 0.3140,  0.4808, -0.3196],
        [-0.2363, -0.8024,  1.4464],
        [ 0.5930,  0.3348,  0.0395]])

Tensor on GPU:
tensor([[ 0.3140,  0.4808, -0.3196],
        [-0.2363, -0.8024,  1.4464],
        [ 0.5930,  0.3348,  0.0395]], device='cuda:0')
GPU tensor device: cuda:0
```

## 機能

- PyTorchとTorchvisionのバージョン確認
- CUDA利用可能性の確認
- GPU情報の表示
- CPU/GPU上でのテンソル操作のテスト

## システム要件

- Python >= 3.12
- NVIDIA GPU (CUDA対応)
- CUDA 12.8 ドライバー

## 参考資料

このプロジェクトは以下の公式ドキュメントを参考にして作成されました：

- [uv PyTorch統合ガイド](https://docs.astral.sh/uv/guides/integration/pytorch/)

## uvを使うメリット

1. **自動的な最適化**: Linux環境でCUDA対応版を自動選択
2. **依存関係管理**: 複雑なPyTorchエコシステムを適切に管理
3. **高速インストール**: 効率的なパッケージ解決とダウンロード
4. **環境の再現性**: `pyproject.toml`と`uv.lock`による確実な環境再現

## プロジェクト構造

```
uv-torch-install/
├── main.py           # PyTorchテストスクリプト
├── pyproject.toml    # プロジェクト設定
├── uv.lock          # 依存関係ロックファイル
└── README.md        # このファイル
```

## トラブルシューティング

### CUDAが認識されない場合

1. NVIDIA ドライバーが正しくインストールされているか確認
2. CUDA 12.8 対応ドライバーがインストールされているか確認
3. `nvidia-smi` コマンドでGPUが認識されているか確認

### インストールに失敗する場合

```bash
# uvのバージョンを確認（0.5.3以降が推奨）
uv --version

# キャッシュをクリアして再試行
uv cache clean
uv sync --reinstall
```
