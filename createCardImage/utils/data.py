from .style import styles


def combine(elements):  # Puts all the tools in span tags and puts them in here
    elString = ""
    for el in elements:
        elString += f"<span>{el}</span>\n"

    return elString

# Fill in information about the project


def collectData():
    count = 1
    spanTags = []  # The skills used to complete project will be here

    print("------ Create your project card ------")
    projectName = input("Enter project name: ")
    description = input("\nEnter project description: ")

    print("\nEnter the tech stack you've used in the project (x to stop):")

    while (True):
        tool = input(f"{count}. ")
        if tool.lower() == "x":
            break
        spanTags.append(tool)
        count += 1

    image = input("\nEnter an image path or link: ")

    return {"projectName": projectName, "description": description, "image": image, "spanTags": spanTags}


def createHtml(data):
    html = f"""
    {styles}
    <div class="card">
        <img src={data.get("image")} />
        <div class="project-info">
            <h2>{data.get("projectName")}</h2>
            <p>{data.get("description")}</p>
            <div class="tools">
                {combine(data.get("spanTags"))}
            </div>
        </div>
    </div>
    """

    return html
