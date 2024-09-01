import React, { useState } from 'react';
import EmojiSelector from './components/EmojiSelector';
import EmojiCombiner from './components/EmojiCombiner';
import EmojiDisplay from './components/EmojiDisplay';
import { combineEmojis } from './utils/emojiUtils';
import './App.css';

const App: React.FC = () => {
  const [selectedEmojis, setSelectedEmojis] = useState<string[]>([]);
  const [combinedEmoji, setCombinedEmoji] = useState<string | null>(null);

  const handleEmojiSelect = (emoji: string) => {
    if (selectedEmojis.length < 2) {
      setSelectedEmojis([...selectedEmojis, emoji]);
    }
  };

  const handleCombine = () => {
    if (selectedEmojis.length === 2) {
      const result = combineEmojis(selectedEmojis[0], selectedEmojis[1]);
      setCombinedEmoji(result);
    }
  };

  const handleReset = () => {
    setSelectedEmojis([]);
    setCombinedEmoji(null);
  };

  return (
    <div className="App">
      <h1>🧑‍🍳 Emoji Kitchen</h1>
      <EmojiSelector onSelect={handleEmojiSelect} />
      <EmojiCombiner 
        selectedEmojis={selectedEmojis} 
        onCombine={handleCombine}
        onReset={handleReset}
      />
      {combinedEmoji && <EmojiDisplay emoji={combinedEmoji} />}
    </div>
  );
};

export default App;