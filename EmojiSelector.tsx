import React from 'react';

interface EmojiSelectorProps {
  onSelect: (emoji: string) => void;
  emojis: string[];
}

const EmojiSelector: React.FC<EmojiSelectorProps> = ({ onSelect, emojis }) => {
  return (
    <div>
      {emojis.map((emoji) => (
        <button key={emoji} onClick={() => onSelect(emoji)}>
          {emoji}
        </button>
      ))}
    </div>
  );
};

export default EmojiSelector;
