import metadata from '../metadata.json';

export const combineEmojis = (emoji1: string, emoji2: string): string | null => {
  const combination = metadata[emoji1]?.[emoji2] || metadata[emoji2]?.[emoji1];
  
  if (combination) {
    return `https://www.gstatic.com/android/keyboard/emojikitchen/${combination}`;
  }
  
  return null;
};
