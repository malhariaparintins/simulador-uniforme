app.py
import streamlit as st
from PIL import Image, ImageDraw
import io

st.set_page_config(page_title="Simulador de Uniforme", layout="centered")
st.title("👕 Simulador de Uniforme")
st.markdown("Envie um mockup base (.png) para aplicar cor personalizada e estampa.")

uploaded_file = st.file_uploader("📤 Envie o mockup (PNG)", type=["png"])
if uploaded_file:
    mockup = Image.open(uploaded_file).convert("RGBA")
    overlay = Image.new("RGBA", mockup.size, (0, 102, 204, 120))
    custom_mockup = Image.alpha_composite(mockup, overlay)
    draw = ImageDraw.Draw(custom_mockup)
    circle_position = (mockup.size[0] // 3, 100, mockup.size[0] // 3 + 100, 200)
    draw.ellipse(circle_position, fill=(255, 0, 0, 200))
    st.subheader("🖼️ Mockup Customizado:")
    st.image(custom_mockup)
    buf = io.BytesIO()
    custom_mockup.save(buf, format="PNG")
    st.download_button("📥 Baixar imagem final", data=buf.getvalue(),
                       file_name="mockup_customizado.png", mime="image/png")
