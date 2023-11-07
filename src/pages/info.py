from src.pages import data_page, home_page, pdf_page, results_page, search_page


class PageInfo:
    home_page = {
        "text": "主页 / Home",
        "target": "/",
        "page": home_page,
    }
    pdf_page = {
        "text": "PDF 查看 / PDF Viewer",
        "target": "/pdf_viewer",
        "page": pdf_page,
    }
    data_page = {
        "text": "数据分析 / Data Analysis",
        "target": "/data_analysis",
        "page": data_page,
    }
    results_page = {
        "text": "结果分析 / Results",
        "target": "/results",
        "page": results_page,
    }
    search_page = {
        "text": "数据搜索 / Search",
        "target": "/search",
        "page": search_page,
    }
