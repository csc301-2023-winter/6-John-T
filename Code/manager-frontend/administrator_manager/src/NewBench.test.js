import React from 'react';
import ReactDom from 'react-dom';
import renderer from 'react-test-renderer';
import NewBench from '../src/NewBench/NewBench';
it('renders correctly', () => {
   const tree = renderer
    .create(NewBench)
    .toJSON();
  expect(tree).toMatchSnapshot(); 
});