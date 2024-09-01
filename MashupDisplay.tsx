import React from 'react';
import './MashupDisplay.css';

interface MashupDisplayProps {
  mashup: string;
}

const MashupDisplay: React.FC<MashupDisplayProps> = ({ mashup }) => {
  return (
    <div className="mashup-display">
      <h2>Your Emoji Mashup</h2>
      <img src={mashup} alt="Emoji Mashup" />
    </div>
  );
};

export default MashupDisplay;
