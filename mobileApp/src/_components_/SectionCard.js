import React from 'react';
import { Dimensions } from 'react-native';
import styled from 'styled-components/native';
import colors from './Global/colors';

export const DEVICE_WIDTH = Dimensions.get('window').width;

const Card = styled.View`
  width: ${DEVICE_WIDTH - 10};
  background-color: ${colors.white};
  padding-left: 10;
  border-radius: 3;
  margin-top: 10;
  align-self: flex-end;
`;

const CardTitle = styled.Text`
  color: ${colors.black};
  font-style: normal;
  font-weight: bold;
  line-height: 16px;
  font-size: 16px;
  letter-spacing: -0.0738462px;
  margin-bottom: 12;
  margin-top: 16;
`;

const SectionCard = ({ title, children, ...props }) => (
  <Card {...props}>
    {title && <CardTitle>{title}</CardTitle>}
    {children}
  </Card>
);

export default SectionCard;
