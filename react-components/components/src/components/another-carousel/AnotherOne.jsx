import React, { useState } from 'react';
import styled from 'styled-components';

// I don't code like this. Just to lazy to create another folder for styles😂
const ComponentContainer = styled.div`
  width: 100%;
  height: 100vh;
  backdrop-filter: blur(2px) brightness(50%);
  display: flex;
`;

const CarouselContainer = styled.div`
  margin: auto;
  width: 100%;
  height: 60%;
  position: relative;
`;

const ImgContainer = styled.div`
  width: 80%;
  height: 80%;
  margin: 0 auto;

  img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    object-position: center center;
  }
`;

const PreviewContainer = styled.div`
  display: flex;
  justify-content: center;
  margin: 2rem auto;
`;

const PreviewImageContainer = styled.div`
  width: 3rem;
  height: 3rem;

  z-index: ${(props) => (props.active ? '10' : '0')};

  img {
    width: 100%;
    height: 100%;
    transform: ${(props) => (props.active ? 'scale(1)' : 'scale(0.9)')};
    outline: 2px solid ${(props) => (props.active ? 'white' : 'transparent')};
    transition: all 0.2s;
    object-fit: cover;
  }
`;

const NextBtn = styled.span`
  position: absolute;
  top: 40%;
  right: 1rem;
`;

const PrevBtn = styled.span`
  position: absolute;
  top: 40%;
  left: 1rem;
`;

const AnotherOne = (props) => {
  const { photos } = props;

  const [current, setCurrent] = useState(0);
  const [startPosition, setStartPosition] = useState(0);
  const [endPosition, setEndPosition] = useState(0);

  console.log(startPosition, endPosition);

  const touchStart = (e) => {
    const startPos = e.touches[0].clientX;

    setStartPosition(startPos);
  };

  const touchMove = (e) => {
    setEndPosition(e.touches[0].clientX);
  };

  const touchEnd = (e) => {
    const currentPos = startPosition - endPosition;

    if (currentPos > 0) {
      setCurrent((current + 1) % photos.length);
    } else if (currentPos < 0) {
      if (current === 0) {
        setCurrent(photos.length - 1);
      } else {
        setCurrent(current - 1);
      }
    }

    setStartPosition(0);
    setEndPosition(0);
  };

  const onNextClick = () => {
    setCurrent((current + 1) % photos.length);
  };

  const onPrevClick = () => {
    setCurrent((current - 1) % photos.length);
  };

  return (
    <ComponentContainer>
      <CarouselContainer
        onTouchStart={touchStart}
        onTouchMove={touchMove}
        onTouchEnd={touchEnd}
      >
        <ImgContainer>
          <img src={photos[current]} alt='test' />
        </ImgContainer>

        <NextBtn onClick={onNextClick}>Next</NextBtn>
        <PrevBtn onClick={onPrevClick}>Prev</PrevBtn>

        <PreviewContainer className='prev-images'>
          {photos.map((image, index) => {
            return (
              <PreviewImageContainer
                key={index}
                active={index === current}
                className='prev-img-container'
              >
                <img src={image} alt='' />
              </PreviewImageContainer>
            );
          })}
        </PreviewContainer>
      </CarouselContainer>
    </ComponentContainer>
  );
};

export default AnotherOne;
