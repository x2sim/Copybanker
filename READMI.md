# Copybanker

## Приложение позволяет сохранять в буфере обмена несколько независимых объектов


**Как установить**

* Python должен быть установлен.
* Затем в командной строке используйте pip (или pip3, есть конфликт с Python2) 
для установки зависимостей: `pip install -r requirements.txt`


**Интерфейс программы**

<a href="https://imgbb.com/"><img src="https://i.ibb.co/10whGjP/1.jpg" alt="1" border="0"></a>
* Интерфейс программы состоит из программируемых кнопок памяти 
(вертикальный ряд из 8-ми кнопок), слайдера прозрачности окна, области для ввода текста
и кнопок удаления информации.

**Как пользоваться**

* Запуск программы производится командой `copybanker.py`
* Каждая кнопка памяти может хранить одновременно 2 вида информации: название и значение. 

<a href="https://imgbb.com/"><img src="https://i.ibb.co/pw4Hdwz/4.jpg" alt="4" border="0"></a>

* Значение кнопки отображается при наведении на нее курсора мыши, в остальных случаях кнопка
отображает название. Это  бывает удобно, когда пытаешься использовать несколько однотипных данных,
доустим ip абонента, ip коммутатора и т.д. Если записать в кнопки только значения, то по
ним трудно будет определить какой ip относится к абоненту, а какой к коммутатору.
Поэтому почти во всех случаях кнопка будет отображать лишь название, но если вам необходимо 
увидеть ее значение, то достаточно навести на нее курсор.
* Для занесения значения в кнопку достаточно навести на нее курсор и нажать правую кнопку 
мыши (предварительно в буфере обмена уже должна быть информация)
* Для занесения названия в кнопку, ее имя нужно напечатать в строке ввода текста и затем
нажать ту кнопку, которой вы хотите присвоить это имя. 

<a href="https://imgbb.com/"><img src="https://i.ibb.co/ByDq3Vc/3.jpg" alt="3" border="0"></a>

* После занесения имени необходимо 
очистить строку ввода, нажав кнопку "clear". Пока строка вода будет заполнена, в 
кнопки будут заносится имена.
* Для того, чтобы скопировать в буфер обмена значение кнопки, нужно навести на нее 
курсор и нажать правую кнопку мыши.
* Для удаления всей информации со всех кнопок, нужно нажать кнопку "Х" 
* Чтобы вам не приходилось делать лишних действий, окно программы всегда находится
поверх остальных. В случае, если окно программы закрывает обзор какого либо документа,
передвиньте его, зажав левую клавишу мыши над названием окна и переместите в удобное место.
Вы также можете настроить прозрачность окна программы, используя положение слайдера:
<a href="https://ibb.co/DLSMsXp"><img src="https://i.ibb.co/GFbMBwT/2.jpg" alt="2" border="0"></a>




**Цель проекта**

Практика в освоении фреймворка PyQt5, модулей по работе с буфером памяти, ускорение
работы.
