import Enzyme, {shallow} from 'enzyme';
import Adapter from 'enzyme-adapter-react-16';
import BenchList from '../BenchList/BenchList'
import { BrowserRouter as Router} from 'react-router-dom';
import toJson from 'enzyme-to-json';

Enzyme.configure({adapter: new Adapter()});

test('renders learn react link', () => {
  const test = shallow(<Router><BenchList/></Router>);
  expect(toJson(test)).toMatchSnapshot();
});
