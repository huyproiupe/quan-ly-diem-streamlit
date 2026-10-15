import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 1. Tiêu đề Web App
st.title("QUẢN LÝ ĐIỂM SINH VIÊN")

# Dữ liệu
ho_ten = ["An", "Bình", "Chi", "Dũng", "Hà", "Lan", "Minh", "Nam", "Phúc", "Trang"]
chuyen_can = [9.0, 8.5, 7.0, 9.5, 8.0, 6.0, 8.5, 7.5, 8.0, 9.0]
giua_ky = [8.0, 8.5, 6.5, 9.0, 7.0, 5.5, 8.0, 6.5, 7.0, 9.0]
cuoi_ky = [8.0, 8.5, 6.0, 9.0, 7.5, 6.0, 8.5, 7.0, 7.5, 9.0]

tong_ket = []
for i in range(len(ho_ten)):
    dtk = 0.2 * chuyen_can[i] + 0.3 * giua_ky[i] + 0.5 * cuoi_ky[i]
    tong_ket.append(round(dtk, 2))

xep_loai = []
for d in tong_ket:
    if d >= 8.5:
        xep_loai.append("Giỏi")
    elif d >= 7.0:
        xep_loai.append("Khá")
    elif d >= 5.0:
        xep_loai.append("Trung bình")
    else:
        xep_loai.append("Yếu")

df = pd.DataFrame({
    'Họ và tên': ho_ten,
    'Chuyên cần': chuyen_can,
    'Giữa kỳ': giua_ky,
    'Cuối kỳ': cuoi_ky,
    'Tong_ket': tong_ket,
    'Xep_loai': xep_loai
})

# 2. Hiển thị bảng điểm
st.subheader("Bảng điểm 10 sinh viên")
st.dataframe(df)

# 3. Thống kê
st.subheader("Thông tin thống kê")
dtb_lop = round(df['Tong_ket'].mean(), 2)
sv_max = df[df['Tong_ket'] == df['Tong_ket'].max()]
sv_min = df[df['Tong_ket'] == df['Tong_ket'].min()]
so_sv_dat = len(df[df['Tong_ket'] >= 5.0])

st.write(f"- Điểm trung bình cả lớp: **{dtb_lop}**")
st.write(f"- Sinh viên điểm cao nhất: **{sv_max['Họ và tên'].values[0]}** ({sv_max['Tong_ket'].values[0]} điểm)")
st.write(f"- Sinh viên điểm thấp nhất: **{sv_min['Họ và tên'].values[0]}** ({sv_min['Tong_ket'].values[0]} điểm)")
st.write(f"- Số sinh viên đạt (>=5): **{so_sv_dat}**")

# 4. Danh sách chọn sinh viên (Selectbox)
st.subheader("Tra cứu thông tin chi tiết")
selected_sv = st.selectbox("Chọn một sinh viên:", df['Họ và tên'])
sv_info = df[df['Họ và tên'] == selected_sv].iloc[0]

st.write(f"- **Chuyên cần:** {sv_info['Chuyên cần']}")
st.write(f"- **Giữa kỳ:** {sv_info['Giữa kỳ']}")
st.write(f"- **Cuối kỳ:** {sv_info['Cuối kỳ']}")
st.write(f"- **Điểm tổng kết:** {sv_info['Tong_ket']}")
st.write(f"- **Xếp loại:** {sv_info['Xep_loai']}")

# 5. Biểu đồ cột
st.subheader("Biểu đồ điểm tổng kết")
fig, ax = plt.subplots(figsize=(8, 4))
ax.bar(df['Họ và tên'], df['Tong_ket'], color='skyblue')
ax.set_ylabel("Điểm tổng kết")
ax.set_ylim(0, 10)
st.pyplot(fig)

# 6. Họ tên & MSSV ở cuối trang (chữ nhỏ)
st.caption("Thực hiện bởi: Trần Quốc Huy - MSSV: 054208007853")