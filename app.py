import streamlit as st
from PIL import Image, ImageDraw

# Dữ liệu mộ phần được viết trực tiếp trong mã
graves = [
    {
        "id": "M001",
        "name": "Nguyễn Văn A",
        "birthYear": 1945,
        "deathYear": 1972,
        "location": "Khu A - Dãy 3 - Số 12",
        "mapCoords": {"x": 100, "y": 150},
        "imageUrl": "",
        "note": "Liệt sĩ hy sinh năm 1972 tại Quảng Trị"
    },
    {
        "id": "M002",
        "name": "Trần Thị B",
        "birthYear": 1950,
        "deathYear": 1990,
        "location": "Khu B - Dãy 2 - Số 7",
        "mapCoords": {"x": 250, "y": 100},
        "imageUrl": "",
        "note": "Người mẹ hiền từ, mất năm 1990"
    },
    {
        "id": "M003",
        "name": "Lê Văn C",
        "birthYear": 1930,
        "deathYear": 1985,
        "location": "Khu C - Dãy 1 - Số 3",
        "mapCoords": {"x": 300, "y": 200},
        "imageUrl": "",
        "note": "Ông Lê Văn C - sống nhân hậu, mất năm 1985"
    },
    {
        "id": "M004",
        "name": "Phạm Thị D",
        "birthYear": 1960,
        "deathYear": 2001,
        "location": "Khu D - Dãy 4 - Số 9",
        "mapCoords": {"x": 150, "y": 230},
        "imageUrl": "",
        "note": "Bà Phạm Thị D - mất năm 2001 vì bệnh"
    },
    {
        "id": "M005",
        "name": "Ngô Văn E",
        "birthYear": 1920,
        "deathYear": 1946,
        "location": "Khu A - Dãy 5 - Số 1",
        "mapCoords": {"x": 80, "y": 180},
        "imageUrl": "",
        "note": "Liệt sĩ kháng chiến chống Pháp"
    }
]

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
