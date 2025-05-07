import gdown
import os

# モデル保存フォルダを作成（なければ）
os.makedirs("models", exist_ok=True)

# Google DriveファイルID
file_id = "17eDcWF_sllLadueyK8Z3K6h82Jl9O4xg"

# ダウンロード先パス
output = "models/model.h5"

# モデルをGoogle Driveからダウンロード
gdown.download(f"https://drive.google.com/uc?id={file_id}", output, quiet=False)