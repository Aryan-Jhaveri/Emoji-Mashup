import React from 'react';

interface EmojiCombinerProps {
  selectedEmojis: string[];
  onCombine: () => void;
  onReset: () => void;
}

const EmojiCombiner: React.FC<EmojiCombinerProps> = ({ selectedEmojis, onCombine, onReset }) => {
  return (
    <div className="emoji-combiner">
      <div className="selected-emojis">
        {selectedEmojis.map((emoji, index) => (
          <span key={index} className="selected-emoji">{emoji}</span>
        ))}
      </div>
      <button onClick={onCombine} disabled={selectedEmojis.length !== 2}>
        Combine
      </button>
      <button onClick={onReset}>Reset</button>
    </div>
  );
};

export default EmojiCombiner;
