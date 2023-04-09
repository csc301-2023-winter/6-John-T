import React from 'react';
import ReactDom from 'react-dom';
import renderer from 'react-test-renderer';
import NewPark from '../src/NewPark/NewPark';
it('renders correctly', () => {
   const tree = renderer
    .create(NewPark)
    .toJSON();
  expect(tree).toMatchSnapshot(); 
});