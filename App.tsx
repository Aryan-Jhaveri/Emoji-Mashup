import React, { useState } from 'react';
import EmojiSelector from './components/EmojiSelector';
import MashupDisplay from './components/MashupDisplay';
import { generateMashup } from './utils/mashupUtils';
import './App.css';

const App: React.FC = () => {
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
    <div className="App">
      <h1>Emoji Mashup Generator</h1>
      <div className="emoji-selectors">
        <EmojiSelector onSelect={setEmoji1} selectedEmoji={emoji1} />
        <EmojiSelector onSelect={setEmoji2} selectedEmoji={emoji2} />
      </div>
      <button onClick={handleGenerate} disabled={!emoji1 || !emoji2}>
        Generate Mashup
      </button>
      {mashupResult && <MashupDisplay mashup={mashupResult} />}
    </div>
  );
};

export default App;
