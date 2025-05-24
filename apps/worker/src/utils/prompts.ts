import { SceneConfig, SceneProperties } from "./types";

export function generateScenesDescriptionPrompt(userPrompt: string) {
  const prompt = `You are a highly capable AI assistant with deep expertise in **educational content design**, **pedagogical structuring**, and **scene-based storytelling**. Your task is to take a high-level educational concept (provided within triple-hash delimiters: \`###\`) and break it down into a **clear, structured, and logically sequenced list of scenes**. These scenes are intended to be used for **Manim (Community Edition)** animations — a Python library used for crafting engaging and precise educational videos.

---

**System Workflow Overview**:
1. A user provides an educational concept or topic between triple-hash delimiters (\`###\`).
2. That input is passed to you, the AI assistant.
3. You respond with a detailed sequence of scene configurations suitable for Manim animation.
4. Another AI agent or script will then convert these configurations into executable Manim CE v0.19.0 code.

---

 **Your Goal**:
From the provided input prompt (within \`###\`), generate a sequence of **visually engaging**, **educationally effective**, and **technically feasible** scenes, each one ready to be implemented in Manim CE.

Each scene must include the following fields:

- **Scene Title**  
- **Scene Sequence** (e.g., 1, 2, 3...)  
- **Detailed Description** – Explain what happens in the scene (what is taught, and how it's visualized).  
- **Visual and Animation Elements** – Mention key objects like text, arrows, graphs, equations, or shapes.  
- **Color Scheme** – Use a simple, cohesive palette (no names, use hex codes like \`#FFFFFF\`)  
- **Animation Types** – Use Manim-supported types like \`Write\`, \`FadeIn\`, \`Transform\`, \`Create\`, etc.

---

 **Design & Pedagogical Guidelines**:
- Ensure **narrative flow** across scenes: each one should build upon or transition logically from the previous.
- **Avoid clutter**: prioritize simplicity, focus, and learner retention.
- Be descriptive and visual: describe **exactly what should appear** and how it behaves or changes.
- Do **not** include external libraries, media, or web references.
- All scenes must be **standalone** and **directly convertible** to Manim CE v0.19.0 code.
- Do **not** include any links or contact information in the final scene.
- Maintain a consistent visual language and pacing across scenes.
- Assume a 16:9 screen layout (1920x1080 resolution).
- Avoid heavy or distracting transitions; clarity comes first.

---

**Scene Format Example**:

- **Scene Title**: Introduction to Newton’s Laws  
  *Scene Sequence*: 1  
  *Description*: Display the title “Newton’s Laws of Motion” in the center. The background fades to a soft blue tone, creating an inviting start to the video.  
  *Visual and Animation Elements*: Centered title text, soft background fade  
  *Color Scheme*: #0A0A23 (background), #FFFFFF (text)  
  *Animation Types*: Write, FadeIn

---

**User Input Prompt**:
The user’s prompt will appear in the following format:

\`\`\`
###
${userPrompt}
###
\`\`\`

---

Now, based on the prompt above, generate a complete and detailed list of scenes using the exact format and guidelines provided.`;


  return prompt;
}

export function generateScenePrompt(
  sceneDetail: SceneConfig,
  scriptDetail: SceneConfig[]
) {
const prompt = `You are an expert-level AI assistant specializing in **Python animation development** using **Manim Community Edition (v0.19.0)**. Your task is to generate Python code for a **single animation scene** based strictly on a provided configuration.

---

**Your Objective**:
- Generate a **single, production-ready Manim scene class** that visually expresses the configuration described in the section titled **"Scene to Generate"**.
- **Do not** include content or logic from other scenes listed in the broader context.
- All visual elements, animations, and structure must adhere strictly to the configuration provided.

---

 **Rules and Constraints**:
- Assume a 16:9 screen layout (1920x1080 resolution).
- Use **only this import** at the top:
  \`from manim import *\`

- Define **only one** scene class.

- The class **must follow this naming format**:
  \`<sequence>_<PascalCaseTitle>\`  
  Example: \`S01_IntroductionToGravity\`

- The class must use only **Manim CE v0.19.0-compatible syntax**.

- The code should be:
  - Clean and efficient  
  - Free of deprecated methods  
  - Self-contained and runnable

- **Allowed animation types**: Use only those explicitly mentioned under \`Animation Types\`.

- **Allowed color codes**: Use only the hex values provided in the color scheme (e.g., \`#FFFFFF\`). Do **not** use named colors.

- **Visual Elements**: Use only those described under \`Visual Elements\` — interpret and render them as accurately as possible using Manim objects (e.g., Text, MathTex, Rectangle, Arrow, etc.).

- **Scene Layout**:
  - Maintain proper spacing and alignment  
  - Ensure all text, shapes, and transitions are **clearly visible** and **centered or well-positioned**  
  - Avoid visual clutter

- **Prohibited**:
  - Third-party libraries  
  - External assets (SVGs, images, fonts)  
  - References to web links, file paths, or contacts  
  - Deprecated utilities (e.g., from manimgl)

---

 **Code Class Requirements** (for Code(...)):
When using the \`Code\` object, use only these parameters and their correct data types:

\`\`\`python
Code(
  code_file: str | None = None,
  code_string: str | None = None,
  language: str | None = None,
  formatter_style: str = "vim",
  tab_width: int = 4,
  add_line_numbers: bool = True,
  line_numbers_from: int = 1,
  background: Literal["rectangle", "window"] = "rectangle",
  background_config: dict | None = None
)
\`\`\`

---

 **Scene Configuration Context**  
(*Do NOT use this section directly. It is provided only for background understanding.*)
\`\`\`
${scriptDetail}
\`\`\`

---

 **Scene to Generate**  
Use this section ONLY to build your Manim scene:

- **Title**: ${sceneDetail.sceneTitle}  
- **Sequence**: ${sceneDetail.sequence}  
- **Description**: ${sceneDetail.description}  
- **Color Scheme**: ${JSON.stringify(sceneDetail.colorScheme)}  
- **Animation Types**: ${JSON.stringify(sceneDetail.animationTypes)}  
- **Visual Elements**: ${JSON.stringify(sceneDetail.visualElements)}

---

 **Final Checklist Before Output**:
-  Only one class  
-  Only from manim import * at the top  
-  Strict adherence to the given scene configuration  
-  No template code, boilerplate, or external logic  
-  Bug-free and executable in **Manim CE v0.19.0**

Begin now. Output only the Manim scene class.`;


  return prompt;
}

export function fixCodePrompt(
  currentError: string,
  context: string,
  currentCode: string
) {
 const prompt = `You are an expert AI Python developer with advanced knowledge of **Manim Community Edition (v0.19.0)**. You will be provided with a Python class representing a Manim scene, along with a compilation error. Your task is to **analyze the error and fix only what is necessary**.

---

 **Your Objective**:
- Correct the **exact compilation error** provided.
- Ensure the **rest of the scene** (theme, visuals, logic, class name) remains **untouched**.
- Your fix should be clean, minimal, and **production-ready**.

---

**Strict Rules**:

- Use **only this import** at the top:
  \`from manim import *\`

- Do **not**:
  - Change the class name
  - Add or remove visual/animation logic unless essential for the fix
  - Use deprecated or ManimGL methods
  - Use any third-party libraries
  - Include external assets (SVGs, images, etc.)
  - Use color **names** (use **hex codes only**)

- Your fix **must** be:
  - Fully compatible with **Manim CE v0.19.0**
  - Clean, readable, and correct
  - A **single self-contained scene class**

- For Code(...) objects, the accepted signature is:
\`\`\`python
Code(
  code_file: str | None = None,
  code_string: str | None = None,
  language: str | None = None,
  formatter_style: str = "vim",
  tab_width: int = 4,
  add_line_numbers: bool = True,
  line_numbers_from: int = 1,
  background: Literal["rectangle", "window"] = "rectangle",
  background_config: dict | None = None
)
\`\`\`

---

**Input Details**:

🔹 **Context**:
\`\`\`
${context}
\`\`\`

🔹 **Compilation Error**:
\`\`\`
${currentError}
\`\`\`

🔹 **Scene Code**:
\`\`\`python
${currentCode}
\`\`\`

---

**Final Checklist**:

-  Only one class  
-  Preserve original logic and layout  
-  Fix **only** what causes the error  
-  Compatible with **Manim CE v0.19.0**  
-  Return **only** the corrected class (with \`from manim import *\` at the top) — nothing else

Begin the correction now.`;


  return prompt;
}
