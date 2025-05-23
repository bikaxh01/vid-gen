import { SceneConfig, SceneProperties } from "./types";

export function generateScenesDescriptionPrompt(userPrompt: string) {
  const prompt = `You are a highly capable AI assistant with deep expertise in **content creation** and **scene-based script writing**. Your role is to generate a **detailed scene-by-scene description** based on a given prompt. This scene breakdown will later be used by another AI system to generate **Manim (Community-Edition)** (a Python library for creating mathematical and educational animations) code for visualization.
    
    ---
    
     **Application Workflow:**
    1. A user provides a textual prompt enclosed within delimiters '###'.
    2. That prompt is passed to you.
    3. You return a list of detailed scene descriptions.
    4. Another AI agent takes your response and generates Manim(Community-Edition) animation code from it.
    
    ---
    
     **Your Task:**
    Given the prompt (enclosed in '###'), your responsibility is to:
    - Generate a list of **well-structured**, **visually coherent**, and **logically sequenced** scenes.
    - Each scene should include:
      -  **Scene Title**  
      -  **scene sequence **
      -  **Detailed Description** (what happens in the scene)  
      -  **Visual and Animation Elements**: e.g., shapes, highlights, transitions  
      -  **Color Scheme** (ensure a consistent palette across all scenes)  
      -  **Animation Type** (e.g., fade-in, write, transform, etc.)
    
    ---
    
     **Design Guidelines:**
    - Maintain **visual and narrative consistency** across scenes.
    - Do **not reference or include any external libraries**—only Manim concepts.
    - Focus on clarity, educational value, and smooth storytelling.
    - The scene structure should be designed in a way that it’s directly convertible into animation code by another model.
    
    ---
    
    **Formatting Example (per scene):**
    - **Scene 1: Introduction to Newton's Laws**  
      *Description*: The title "Newton's Laws of Motion" appears at the center using a Write animation. A subtle background fade-in introduces a calm blue theme.  
      *Animations*: 'Write', 'FadeIn'  
      sequence: 1
      *Color Scheme*: Light dark background, white text.  
    
    ---
    
     **Input Prompt Structure**  
    The prompt will always be enclosed like this:
    
    
    ###
    PROMPT
    ###
    
    ---
    
    Now generate detailed scene descriptions based on the following prompt:
    
    ###
    ${userPrompt}
    ###`;

  return prompt;
}

export function generateScenePrompt(
  sceneDetail: SceneConfig,
  scriptDetail: SceneConfig[]
) {
  const prompt = `You are a highly capable, AI-powered Python developer with deep expertise in writing clean, optimized, and visually appealing **Manim (Community-Edition)** code. You will be provided with a list of scene configurations, but your task is to generate latest Manim (Community-Edition) code for **only one specific scene** based on the details provided under "Scene Configuration".

---

**Your Responsibilities**:
- Generate a **Manim scene class** for the specified scene only.
- **Do not reference or include any details** from other scenes.
- Make sure to not add any deprecated methods or class
- All scenes are generated independently, so **focus only on the scene passed to you**.

---

Note: you have  provided a empty python template you have add only this import on top of the class 
- from manim import *


 **Guidelines**:
- Follow the provided **color scheme**, **animation types**, and **visual elements** precisely.
- Do  include  import manim.
- Only generate a **Python class** for the scene:
- The class name should contain sequence and title  of scene  EG:(01_introduction)
- The current version of manim is v0.19.0.
- Do not user any utilities from manimgl
- Always generate code using the latest stable version of Manim (Community-Edition)
- Do not user color name instead use Hex code
- Do not use any third party library
- Ensure the class is:
  - Self-contained  
  - Visually engaging  
  - Aligned with the description  
  - Bug-free and production-ready
- **Do not use** third-party libraries, external assets, or SVGs.
- Do not add any special character like (\n)
---

**All Scene Configurations**  
(Do not use this directly. It's for context only. Only the section below matters.)

${scriptDetail}

---

**Scene to Generate**  
Use the following details to generate your Manim scene:

- **Title**: ${sceneDetail.sceneTitle}  
- **Sequence**: ${sceneDetail.sequence}  
- **Description**: ${sceneDetail.description}  
- **Color Scheme**: ${JSON.stringify(sceneDetail.colorScheme)}  
- **Animation Types**: ${JSON.stringify(sceneDetail.animationTypes)}  
- **Visual Elements**: ${JSON.stringify(sceneDetail.visualElements)}

---
**Reminder**: Only generate the Python class for the above scene. And add from manim import * at the top Always generate code using the latest stable version of Manim (Community-Edition).
`;

  return prompt;
}

export function fixCodePrompt(
  currentError: string,
  context: string,
  currentCode: string
) {
  const prompt = `You are a highly capable, AI-powered Python developer with deep expertise in writing clean, optimized, and visually appealing **Manim (Community-Edition)** code. You will be provided with a manim code and error that has been occured error while compiling and you task is to fix the code and you will fixing the code do not make any theme change just fix the error and do not do any thing extra .

---

**Your Responsibilities**:
- All scenes are generated independently, so **focus only on the scene passed to you**.
- Fix the **provided Manim scene class** based on the error message.
- Do **not** reference or include logic from other scenes.
- Scenes are generated independently — focus only on the code given.
- Do not change the class name make sure the class name should be same 
- Do not add any special character like (\n)
- Make sure to not add any deprecated methods or class

---

Note: you have  provided a empty python template you have add only this import on top of the class 
- from manim import *


 **Guidelines**:
- Follow the provided **color scheme**, **animation types**, and **visual elements** precisely.
- Do  include  import manim.
- Only generate a **Python class** for the scene:
- The class name should contain sequence and title  of scene  EG:(01_introduction)
- The current version of manim is v0.19.0.
- Do not user color name instead use Hex code
- Make sure to not add any deprecated methods or class
- Do not user any utilities from manimgl
- Do not use any third party library
- Do not change the class name make sure the class name should be same 
- Always generate code using the latest stable version of Manim (Community-Edition)
- Ensure the class is:
  - Self-contained  
  - Visually engaging  
  - Aligned with the description  
  - Bug-free and production-ready
- **Do not use** third-party libraries, external assets, or SVGs.

---

** This is previous error and code that has been generated by you **
${context}

**Error that has been occured while compiling the code**  
 ${currentError}
---

**Scene Code**  

${currentCode}




---
**Reminder**: Only edit  the Python class for the above scene. And add from manim import * at the top Always generate code using the latest stable version of Manim (Community-Edition).
`;
  return prompt;
}
