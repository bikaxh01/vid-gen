export interface SceneConfig {
  animationTypes: string[];
  sequence: number;
  colorScheme: {
    background: string;
    highlights: string;
    text: string;
  };
  description: string;
  sceneTitle: string;
  visualElements: string[];
}

export interface SceneProperties {
  sceneTitle: string;
  description: string;
  code: string;
  className: string;
}