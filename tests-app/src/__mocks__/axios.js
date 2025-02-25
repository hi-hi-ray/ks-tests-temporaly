// __mocks__/axios.js

const mockAxios = {
    create: jest.fn(() => mockAxios),
    get: jest.fn(),
    post: jest.fn(),
  };
  
  export default mockAxios;
  