// NOTICE: this is jQuery code, please convert it to the proper framework/library you're using!

const hearts = 12;
const wrapper = $('.js-hearts-animation-wrapper');
const heart = $('.js-mini-profile-heart').detach();

function randomValue(min, max) {
  return (min + Math.random() * (max - min));  
}

function randomHeart(count) {
  const left = (5 + 95/hearts * count).toFixed(2);
  const size = randomValue(18,40).toFixed(2);
  const duration = randomValue(900,1100).toFixed(2);
  const delay = randomValue(0,1200).toFixed(2);
  const style = {
    width: `${size}px`,
    height: `${size}px`,
    left: `${left}%`,
    animationDuration: `${duration}ms`,
    animationDelay: `${delay}ms`
  }
  return heart.clone().css(style);
}

for(let i=0; i<hearts; i++) {
  wrapper.append(randomHeart(i));
}

