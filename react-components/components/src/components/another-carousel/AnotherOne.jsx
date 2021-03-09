import React, { useState, usEffect, useEffect } from 'react';
import styled, { keyframes, css } from 'styled-components';

// I don't code like this. Just to lazy to create another folder for styles😂

const enter = keyframes`

  0% {
    opacity: 0;
  }


  
  100% {
    opacity: 1;
  }

`;
const exit = keyframes`

  0% {
    opacity: 1;
  }


  100% {
    opacity: 0;
  }

`;

const ComponentContainer = styled.div`
  width: 100%;
  height: 100vh;
  backdrop-filter: blur(2px) brightness(50%);
  display: flex;
`;

const CarouselContainer = styled.div`
  margin: auto;
  width: 50%;
  height: 60%;
  position: relative;
`;

const ImgContainer = styled.div`
  width: 80%;
  height: 80%;
  margin: 0 auto;
  display: flex;
  position: relative;
  overflow: hidden;

  img {
    position: absolute;
    width: 100%;
    height: 100%;
    object-fit: cover;
    object-position: center center;
    animation: ${exit} 0.5s ease;
    opacity: 0;
  }

  img.active {
    opacity: 1;
    animation: ${enter} 0.5s ease;
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

  const touchStart = (e) => {
    console.log(e.touches);
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

  useEffect(() => {
    const nextPic = setTimeout(() => {
      onNextClick();
    }, 5000);

    return () => clearTimeout(nextPic);
  }, [current]);

  return (
    <ComponentContainer>
      <CarouselContainer
        onTouchStart={touchStart}
        onTouchMove={touchMove}
        onTouchEnd={touchEnd}
      >
        {/* <ImgContainer>
          <img
            current={active[photos[current]]}
            src={photos[current]}
            alt='test'
          />
        </ImgContainer> */}
        <ImgContainer>
          {photos.map((p, i) => {
            return (
              <img
                className={i === current ? 'active' : ''}
                test={'TEST'}
                key={i}
                src={p}
                alt={p}
              />
            );
          })}
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
