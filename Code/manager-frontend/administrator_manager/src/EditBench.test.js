import React from 'react';
import ReactDom from 'react-dom';
import renderer from 'react-test-renderer';
import EditBench from '../src/EditBench/EditBench';
it('renders correctly', () => {
   const tree = renderer
    .create(EditBench)
    .toJSON();
  expect(tree).toMatchSnapshot(); 
});