import React, { useState } from 'react';
import './EmojiSelector.css';

// This is a placeholder. In a real app, you'd import a complete list of emojis.
const EMOJIS = ['😀', '😂', '😍', '🤔', '😎', '🙈', '🐶', '🐱', '🍕', '🌈'];

interface EmojiSelectorProps {
  onSelect: (emoji: string) => void;
  selectedEmoji: string | null;
}

const EmojiSelector: React.FC<EmojiSelectorProps> = ({ onSelect, selectedEmoji }) => {
  const [searchTerm, setSearchTerm] = useState('');

  const filteredEmojis = EMOJIS.filter(emoji => 
    emoji.toLowerCase().includes(searchTerm.toLowerCase())
  );

  return (
    <div className="emoji-selector">
      <input
        type="text"
        placeholder="Search emojis"
        value={searchTerm}
        onChange={(e) => setSearchTerm(e.target.value)}
      />
      <div className="emoji-grid">
        {filteredEmojis.map((emoji) => (
          <button
            key={emoji}
            onClick={() => onSelect(emoji)}
            className={emoji === selectedEmoji ? 'selected' : ''}
          >
            {emoji}
          </button>
        ))}
      </div>
    </div>
  );
};

export default EmojiSelector;
