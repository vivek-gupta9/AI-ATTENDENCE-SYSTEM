# import streamlit as st


# def footer_home():
#     logo_url = "https://i.ibb.co/4r5X1FY/apnacollege.png"
    
#     st.markdown(f"""
#         <div style="margin-top:2rem; display:flex; gap:6px; justify-content:center; items-align:center">
#         <p style="font-weight:bold; color:white;"> Created with ❤️ by </p>  
#         <img src='{logo_url}' style='max-height:25px' />
#         </div>
                
#                 """, unsafe_allow_html=True)


# def footer_dashboard():
#     logo_url = "https://i.ibb.co/4r5X1FY/apnacollege.png"
    
#     st.markdown(f"""
#         <div style="margin-top:2rem; display:flex; gap:6px; justify-content:center; items-align:center">
#         <p style="font-weight:bold; color:black;"> Created with ❤️ by </p>  
#         <img src='{logo_url}' style='max-height:25px' />
#         </div>
                
#                 """, unsafe_allow_html=True)

import streamlit as st


def footer_home():
    st.markdown("""
        <style>
        .footer-container {
            margin-top: 3rem;
            padding: 1.2rem 0;
            display: flex;
            justify-content: center;
            align-items: center;
        }
        .footer-text {
            font-family: 'Poppins', 'Segoe UI', sans-serif;
            font-size: 15px;
            font-weight: 500;
            color: #ffffff;
            letter-spacing: 0.3px;
        }
        .footer-text a {
            color: #818cf8;
            font-weight: 700;
            text-decoration: none;
            transition: color 0.2s ease;
        }
        .footer-text a:hover {
            color: #a5b4fc;
            text-decoration: underline;
        }
        </style>

        <div class="footer-container">
            <p class="footer-text">
                Made with ❤️ by 
                <a href="https://github.com/vivek-gupta9" target="_blank">Vivek Gupta</a>
            </p>
        </div>
    """, unsafe_allow_html=True)


def footer_dashboard():
    st.markdown("""
        <style>
        .footer-container-dash {
            margin-top: 3rem;
            padding: 1.2rem 0;
            display: flex;
            justify-content: center;
            align-items: center;
        }
        .footer-text-dash {
            font-family: 'Poppins', 'Segoe UI', sans-serif;
            font-size: 15px;
            font-weight: 500;
            color: #1f2937;
            letter-spacing: 0.3px;
        }
        .footer-text-dash a {
            color: #4f46e5;
            font-weight: 700;
            text-decoration: none;
            transition: color 0.2s ease;
        }
        .footer-text-dash a:hover {
            color: #6366f1;
            text-decoration: underline;
        }
        </style>

        <div class="footer-container-dash">
            <p class="footer-text-dash">
                Made with ❤️ by 
                <a href="https://github.com/vivek-gupta9" target="_blank">Vivek Gupta</a>
            </p>
        </div>
    """, unsafe_allow_html=True)