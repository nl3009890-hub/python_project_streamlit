import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Tạo dữ liệu mẫu
data = {
    "Ho_ten": ["Nguyen Van A", "Tran Thi B", "Le Van C", "Pham Thi D", "Hoang Van E",
               "Nguyen Thi F", "Tran Van G", "Le Thi H", "Pham Van I", "Hoang Thi J"],
    "Chuyen_can": [8, 9, 7, 6, 10, 9, 8, 7, 6, 9],
    "Giua_ky": [7, 8, 6, 5, 9, 8, 7, 6, 5, 8],
    "Cuoi_ky": [8, 9, 7, 6, 10, 9, 8, 7, 6, 9]
}

df = pd.DataFrame(data)
df["Tong_ket"] = (df["Chuyen_can"]*0.2 + df["Giua_ky"]*0.3 + df["Cuoi_ky"]*0.5)

def xep_loai(diem):
    if diem >= 8: return "Giỏi"
    elif diem >= 6.5: return "Khá"
    elif diem >= 5: return "Trung bình"
    else: return "Yếu"

df["Xep_loai"] = df["Tong_ket"].apply(xep_loai)

# Giao diện Streamlit
st.title("Quản lý điểm sinh viên")

st.subheader("Bảng điểm lớp")
st.dataframe(df)

st.subheader("Thống kê lớp")
st.write("Điểm trung bình lớp:", round(df["Tong_ket"].mean(), 2))
st.write("SV cao nhất:", df.loc[df["Tong_ket"].idxmax(), "Ho_ten"],
         "- Điểm:", round(df["Tong_ket"].max(), 2))
st.write("SV thấp nhất:", df.loc[df["Tong_ket"].idxmin(), "Ho_ten"],
         "- Điểm:", round(df["Tong_ket"].min(), 2))
st.write("Số SV đạt (>=5):", (df["Tong_ket"] >= 5).sum())

st.subheader("Tra cứu điểm theo sinh viên")
sv = st.selectbox("Chọn sinh viên:", df["Ho_ten"])
sv_info = df[df["Ho_ten"] == sv].iloc[0]
st.write("Chuyên cần:", sv_info["Chuyen_can"])
st.write("Giữa kỳ:", sv_info["Giua_ky"])
st.write("Cuối kỳ:", sv_info["Cuoi_ky"])
st.write("Tổng kết:", round(sv_info["Tong_ket"], 2))
st.write("Xếp loại:", sv_info["Xep_loai"])

st.subheader("Biểu đồ điểm tổng kết")
fig, ax = plt.subplots()
ax.bar(df["Ho_ten"], df["Tong_ket"], color="skyblue")
ax.set_title("Điểm tổng kết của sinh viên")
ax.set_ylabel("Điểm")
plt.xticks(rotation=45)
st.pyplot(fig)

st.markdown("---")
st.write("👨‍💻 Người tạo: Nguyễn Văn Tuấn - MSSV: 123456")
