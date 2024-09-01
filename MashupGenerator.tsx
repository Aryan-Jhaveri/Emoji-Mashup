import React, { useState } from 'react';
import EmojiSelector from './EmojiSelector';
import MashupDisplay from './MashupDisplay';
import { generateMashup } from '../utils/mashupUtils';

const MashupGenerator: React.FC = () => {
  const [emoji1, setEmoji1] = useState<string | null>(null);
  const [emoji2, setEmoji2] = useState<string | null>(null);
  const [mashupResult, setMashupResult] = useState<string | null>(null);

  const handleGenerate = () => {
    if (emoji1 && emoji2) {
      const result = generateMashup(emoji1, emoji2);
      setMashupResult(result);
    }
  };

  return (
    <div>
      <EmojiSelector onSelect={setEmoji1} emojis={/* list of emojis */} />
      <EmojiSelector onSelect={setEmoji2} emojis={/* list of emojis */} />
      <button onClick={handleGenerate}>Generate Mashup</button>
      {mashupResult && <MashupDisplay mashup={mashupResult} />}
    </div>
  );
};

export default MashupGenerator;
