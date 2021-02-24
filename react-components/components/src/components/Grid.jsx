import React from 'react';
import styled, { css } from 'styled-components';

const TwoImageLayout = css`
  grid-template-areas: 'a b';
  grid-template-rows: 1fr;
`;

const OneImageLayout = css`
  grid-template-areas: 'a';
  grid-template-rows: 1fr;
`;

const ThreeImageLayout = css`
  grid-template-areas:
    'a a b'
    'a a c';
  grid-template-rows: repeat(2, 50%);
`;

const ThreePlusLayout = css`
  grid-template-areas:
    'a a b'
    'a a c'
    'a a d';
  grid-template-rows: repeat(3, 33%);
`;

const getNumberOfPhotos = (props) => {
  if (props.length === 1) {
    return OneImageLayout;
  }
  if (props.length === 2) {
    return TwoImageLayout;
  }
  if (props.length === 3) {
    return ThreeImageLayout;
  }
  if (props.length > 3) {
    return ThreePlusLayout;
  }
};

const GridContainer = styled.div`
  width: 50rem;
  height: 30rem;
  outline: 2px solid blue;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  display: grid;
  ${getNumberOfPhotos}
  grid-column-gap: 2px;
  grid-row-gap: 2px;

  overflow: hidden;

  & > :nth-child(1) {
    grid-area: a;
  }

  & > :nth-child(2) {
    grid-area: b;
  }
  & > :nth-child(3) {
    grid-area: c;
  }

  & > :nth-child(4) {
    grid-area: d;
  }
`;

const Image = styled.img`
  height: 100%;
  width: 100%;
  object-fit: cover;
  object-position: center;
`;

const Blocks = styled.div`
  height: 100%;
  width: 100%;
  border: 2px solid black;
`;

const ExtraImage = styled(Blocks)`
  font-size: 2rem;
  color: #fff;
  background-color: #0ca174;
  display: flex;
  align-items: center;
  justify-content: center;
`;

const Grid = (props) => {
  const { photos } = props;

  const areaLabel = ['a', 'b', 'c', 'd'];

  return (
    <GridContainer length={photos.length}>
      {photos.slice(0, 3).map((url) => {
        return (
          <Blocks>
            <Image src={url} alt={url} />
          </Blocks>
        );
      })}

      {photos.length > 3 && (
        <ExtraImage>
          <p>+{photos.length - 3} more</p>
        </ExtraImage>
      )}
    </GridContainer>
  );
};

export default Grid;
