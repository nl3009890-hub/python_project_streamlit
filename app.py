import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ====== DỮ LIỆU ======
data = {
    "Ho_ten": ["An","Bình","Chi","Dũng","Hà","Lan","Minh","Nam","Phúc","Trang"],
    "Chuyen_can": [8,9,7,6,10,9,8,7,6,9],
    "Giua_ky": [7,8,6,5,9,8,7,6,5,8],
    "Cuoi_ky": [8,9,7,6,10,9,8,7,6,9]
}
df = pd.DataFrame(data)

# ====== TÍNH ĐIỂM TỔNG KẾT ======
df["Tong_ket"] = 0.2*df["Chuyen_can"] + 0.3*df["Giua_ky"] + 0.5*df["Cuoi_ky"]

# ====== XẾP LOẠI ======
def xep_loai(d):
    if d >= 8.5: return "Giỏi"
    elif d >= 7: return "Khá"
    elif d >= 5: return "Trung bình"
    else: return "Yếu"
df["Xep_loai"] = df["Tong_ket"].apply(xep_loai)

# ====== GIAO DIỆN STREAMLIT ======
st.title("QUẢN LÝ ĐIỂM SINH VIÊN")

# Hiển thị bảng dữ liệu
st.subheader("Bảng điểm sinh viên")
st.dataframe(df)

# Thống kê
st.subheader("Thống kê lớp")
st.write("Điểm trung bình lớp:", round(df["Tong_ket"].mean(),2))
st.write("SV cao nhất:", df.loc[df["Tong_ket"].idxmax(),"Ho_ten"], 
         "- Điểm:", round(df["Tong_ket"].max(),2))
st.write("SV thấp nhất:", df.loc[df["Tong_ket"].idxmin(),"Ho_ten"], 
         "- Điểm:", round(df["Tong_ket"].min(),2))
st.write("Số SV đạt (>=5):", (df["Tong_ket"]>=5).sum())

# Selectbox chọn sinh viên
st.subheader("Tra cứu điểm theo sinh viên")
sv = st.selectbox("Chọn sinh viên:", df["Ho_ten"])
sv_info = df[df["Ho_ten"]==sv].iloc[0]
st.write("Chuyên cần:", sv_info["Chuyen_can"])
st.write("Giữa kỳ:", sv_info["Giua_ky"])
st.write("Cuối kỳ:", sv_info["Cuoi_ky"])
st.write("Tổng kết:", round(sv_info["Tong_ket"],2))
st.write("Xếp loại:", sv_info["Xep_loai"])

# Biểu đồ cột
st.subheader("Biểu đồ điểm tổng kết")
fig, ax = plt.subplots()
ax.bar(df["Ho_ten"], df["Tong_ket"], color="skyblue")
ax.set_title("Điểm tổng kết của sinh viên")
ax.set_ylabel("Điểm")
st.pyplot(fig)

# Thông tin người tạo
st.markdown("<small>Người tạo: Nguyễn Anh Tuấn - MSSV: 123456</small>", unsafe_allow_html=True)
