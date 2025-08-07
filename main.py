import torch
import torchvision


def main():
    print("Hello from uv-torch-install!")

    # PyTorchのバージョンを表示
    print(f"PyTorch version: {torch.__version__}")
    print(f"Torchvision version: {torchvision.__version__}")

    # CUDAが利用可能かどうかを確認
    print(f"CUDA available: {torch.cuda.is_available()}")
    if torch.cuda.is_available():
        print(f"CUDA version: {torch.version.cuda}")
        print(f"Number of CUDA devices: {torch.cuda.device_count()}")
        print(f"Current CUDA device: {torch.cuda.current_device()}")
        print(f"Device name: {torch.cuda.get_device_name(0)}")

    # 簡単なテンソル操作のテスト
    x = torch.randn(3, 3)
    print(f"\nRandom tensor:\n{x}")

    # GPUが利用可能な場合はGPUでテストを実行
    if torch.cuda.is_available():
        x_gpu = x.cuda()
        print(f"\nTensor on GPU:\n{x_gpu}")
        print(f"GPU tensor device: {x_gpu.device}")


if __name__ == "__main__":
    main()
