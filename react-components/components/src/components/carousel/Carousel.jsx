import React from 'react';

import Slider from 'react-slick';
import styled from 'styled-components';

import 'slick-carousel/slick/slick.css';
import 'slick-carousel/slick/slick-theme.css';

const TestWrapper = styled.div`
  width: 100%;
  height: 100vh;
  display: flex;
  align-items: center;
  flex-direction: column;
  backdrop-filter: blur(10px) brightness(10%);

  justify-content: center;

  .carouselWrapper {
    width: 40%;
    height: 65%;
    border: 1px solid green;
    display: flex;
    align-items: center;
    background: white;
    border-radius: 21.5px;
  }

  .slick-arrow.slick-next:before,
  .slick-arrow.slick-prev:before {
    color: green;
  }

  .slider.variable-width {
    width: 80%;
    height: auto;
    margin: 0 auto;

    img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      object-position: center center;
    }
  }
`;

const Carousel = (props) => {
  const settings = {
    className: 'slider variable-width',
    arrows: true,
    dots: true,
    fade: true,
    infinite: true,
    speed: 500,
    slidesToshow: 1,
    slidesToScroll: 1,
  };

  return (
    <TestWrapper>
      <div className='carouselWrapper'>
        <Slider {...settings}>
          {props.photos.map((p, index) => {
            return (
              <div key={index}>
                <img src={p} alt='test' />
              </div>
            );
          })}
        </Slider>
      </div>
    </TestWrapper>
  );
};

export default Carousel;
