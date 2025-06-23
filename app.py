import streamlit as st
import json
from PIL import Image, ImageDraw

# Load dữ liệu mộ
with open("graves.json", "r", encoding="utf-8") as f:
    graves = json.load(f)["graves"]

st.title("📚 Thư viện Nghĩa Trang")
query = st.text_input("🔍 Nhập tên người đã khuất:")

if query:
    results = [g for g in graves if query.lower() in g["name"].lower()]
    if results:
        for g in results:
            st.subheader(g["name"])
            st.write(f"📍 Vị trí: {g['location']}")
            st.write(f"📜 Ghi chú: {g['note']}")
            st.image(g["imageUrl"] or "https://via.placeholder.com/100", width=200)

            # Hiển thị vị trí trên ảnh sơ đồ
            image = Image.open("map.png").convert("RGBA")
            draw = ImageDraw.Draw(image)
            x, y = g["mapCoords"]["x"], g["mapCoords"]["y"]
            draw.ellipse((x-5, y-5, x+5, y+5), fill=(255, 0, 0, 255))
            st.image(image, caption="Vị trí mộ")
    else:
        st.warning("Không tìm thấy người này.")
                                                  
