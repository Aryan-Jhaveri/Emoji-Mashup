import metadata from './metadata.json';

interface MashupMetadata {
  [key: string]: {
    [key: string]: string;
  };
}

const mashupMetadata: MashupMetadata = metadata;

export const generateMashup = (emoji1: string, emoji2: string): string => {
  if (mashupMetadata[emoji1] && mashupMetadata[emoji1][emoji2]) {
    return mashupMetadata[emoji1][emoji2];
  } else if (mashupMetadata[emoji2] && mashupMetadata[emoji2][emoji1]) {
    return mashupMetadata[emoji2][emoji1];
  } else {
    return 'No mashup available for these emojis';
  }
};
