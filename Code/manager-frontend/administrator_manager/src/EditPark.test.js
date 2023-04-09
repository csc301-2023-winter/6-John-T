import React from 'react';
import ReactDom from 'react-dom';
import renderer from 'react-test-renderer';
import EditPark from '../src/EditPark/EditPark';
it('renders correctly', () => {
   const tree = renderer
    .create(EditPark)
    .toJSON();
  expect(tree).toMatchSnapshot(); 
});