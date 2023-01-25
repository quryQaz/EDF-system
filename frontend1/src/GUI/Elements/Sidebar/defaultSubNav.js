import React from 'react';
import Key from 'styles/icons/key'
import Logs from 'styles/icons/logs'
import User from 'styles/icons/user'
import Clear from 'styles/icons/clear'
import Errors from 'styles/icons/errors'
import Drivers from 'styles/icons/drivers'
import Console from 'styles/icons/console'
import Programs from 'styles/icons/programs'
import Processes from 'styles/icons/processes'
import Disconnect from 'styles/icons/disconnect'

export const defaultSubNav = (ip) =>  {
  return [
      {
        title: 'Список процессов' ,
        itemId: `${ip}/Processes`,
        elemBefore: () => <Processes/>
      },
      {
        title: 'Список драйверов',
        itemId: `${ip}/Drivers`,
        elemBefore: () => <Drivers/>
      },
      {
        title: 'Информация о системе',
        itemId: `${ip}/Registry`,
        elemBefore: () => <Key/>
      },
      {
        title: 'Логи',
        itemId: `${ip}/Logs`,
        elemBefore: () => <Logs/>
      },
      {
        title: 'Статусы ошибок',
        itemId: `${ip}/Errors`,
        elemBefore: () => <Errors/>
      },
      {
        title: 'Информация о ПО',
        itemId: `${ip}/Programs`,
        elemBefore: () => <Programs/>
      },
      {
        title: 'Список пользователей',
        itemId: `${ip}/Users`,
        elemBefore: () => <User/>
      },
      {
        title: 'Консоль',
        itemId: `${ip}/Console`,
        elemBefore: () => <Console/>
      },
      {
        title: 'Очистить',
        itemId: `${ip}/Clear`,
        elemBefore: () => <Clear/>
      },
      {
        title: 'Отключить',
        itemId: `${ip}/Disconnecs`,
        elemBefore: () => <Disconnect/>
      },
]}
