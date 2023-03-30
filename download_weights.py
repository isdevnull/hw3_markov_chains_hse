import os
import gdown

BASE_DIR = "./weights"

def download_gan_weights():
    gan_name_id = (("cifar10_sngan_G.pth", "1EgrCa1PoGE2V4415QsKeMFFPZnsT4QRm"), ("cifar10_sngan_D.pth", "1ZfoTIhLW6QqGFwFXMl41PTcjGwfKCGLg"), ("cifar10_dcgan_G.pth", "1k_DwjkprptuCXK_gJzFF9eUCHTD9vOUH"), ("cifar10_dcgan_D.pth", "1o6cXzpAPhGZxJOJseic8oGhsuilcLdLK"))
    
    os.makedirs(BASE_DIR, exist_ok=True)

    for name, google_id in gan_name_id:
        weight_path = os.path.join(BASE_DIR, name)
        if not os.path.exists(weight_path):
            print(f"Downloading weights {name} to {weight_path}...", flush=True)
            gdown.download(id=google_id, output=weight_path, quiet=False)
        else:
            print(f"Weight {name} is already downloaded!")


if __name__ == "__main__":
    download_gan_weights()
