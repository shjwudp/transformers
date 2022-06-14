torch_versions_testing = [
    {
        "torch": "1.11.0",
        "torchvision": "0.12.0",
        "torchaudio": "0.11.0",
        "python": 3.9,
        "cuda": "11.3",
        "install": "python3 -m pip install --no-cache-dir -U torch==1.11.0 torchvision==0.12.0 torchaudio==0.11.0 --extra-index-url https://download.pytorch.org/whl/cu113",
    },
    {
        "torch": "1.10.2",
        "torchvision": "0.11.3",
        "torchaudio": "0.10.2",
        "python": 3.9,
        "cuda": "11.3",
        "install": "python3 -m pip install --no-cache-dir -U torch==1.10.2 torchvision==0.11.3 torchaudio==0.10.2 --extra-index-url https://download.pytorch.org/whl/cu113",
    }, # OK
    # torchaudio < 0.10 has no CUDA-enabled binary distributions
    {
        "torch": "1.9.1",
        "torchvision": "0.10.1",
        "torchaudio": "0.9.1",
        "python": 3.9,
        "cuda": "11.1",
        "install": "python3 -m pip install --no-cache-dir -U torch==1.9.1 torchvision==0.10.1 torchaudio==0.9.1 --extra-index-url https://download.pytorch.org/whl/cu111",
    },
    {
        "torch": "1.8.1",
        "torchvision": "0.9.1",
        "torchaudio": "0.8.1",
        "python": 3.9,
        "cuda": "11.1",
        "install": "python3 -m pip install --no-cache-dir -U torch==1.8.1 torchvision==0.9.1 torchaudio==0.8.1 --extra-index-url https://download.pytorch.org/whl/cu111",
    },
    {
        "torch": "1.7.1",
        "torchvision": "0.8.2",
        "torchaudio": "0.7.2",
        "python": 3.9,
        "cuda": 11.0,
        "install": "python3 -m pip install --no-cache-dir -U torch==1.7.1 torchvision==0.8.2 torchaudio==0.7.2 --extra-index-url https://download.pytorch.org/whl/cu110",
    },
    {
        "torch": "1.6.0",
        "torchvision": "0.7.0",
        "torchaudio": "0.6.0",
        "python": 3.8,
        "cuda": 10.1,
        "install": "python3 -m pip install --no-cache-dir -U torch==1.6.0 torchvision==0.7.0 torchaudio==0.6.0 --extra-index-url https://download.pytorch.org/whl/cu101",
    },
    {
        "torch": "1.5.1",
        "torchvision": "0.6.1",
        "torchaudio": "0.5.1",
        "python": 3.8,
        "cuda": 10.1,
        "install": "python3 -m pip install --no-cache-dir -U torch==1.5.1 torchvision==0.6.1 torchaudio==0.5.1 --extra-index-url https://download.pytorch.org/whl/cu101",
    },
    {
        "torch": "1.4.0",
        "torchvision": "0.5.0",
        "torchaudio": "0.4.0",
        "python": 3.8,
        "cuda": 10.0,
        "install": "python3 -m pip install --no-cache-dir -U torch==1.4.0 torchvision==0.5.0 torchaudio==0.4.0 --extra-index-url https://download.pytorch.org/whl/cu100",
    },
    # need python 3.7
    # {
    #     "torch": "1.3.1",
    #     "torchvision": "0.4.2",
    #     "torchaudio": None,
    #     "python": 3.7,
    #     "cuda": 10.0,
    #     "docker-base": "10.0-cudnn7-devel-ubuntu18.04",
    #     "install": "python3 -m pip install --no-cache-dir -U torch==1.3.1 torchvision==0.4.2 torchaudio==0.4.0 --extra-index-url https://download.pytorch.org/whl/cu100",
    # },
]
