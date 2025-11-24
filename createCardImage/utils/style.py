cardW = 400
styles = f"""
<style>
    :root{{font-size: 14px}}
    *{{
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }}
    .card{{
        width: {cardW}px;
        height: {cardW}px;
        background-color: black;
        border-radius: 20px;
        border: 2px solid orangered;
        overflow: hidden;
        position: relative;
    }}
    .card img{{
        width: 100%;
        object-fit: contain;
    }}
    .project-info{{
        background-color: black;
        font-family: "Courier New", Courier, monospace;
        padding: 1rem;
        position:absolute;
        bottom: 0;
    }}
    .project-info h2{{
        color: #00d2f2;
        margin-bottom: 1rem;
    }}
    .project-info p{{
        color: #A1A1A1;
        margin-bottom: 1rem;
    }}
    .tools{{
        display: flex;
        flex-wrap: wrap;
        gap: 5px;
    }}
    .tools span{{
        color: white;
        padding: 5px;
        background-color: #181818;
        border-radius: 7px;
        display: block;
    }}
</style>
"""
