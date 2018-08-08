# The PEP 484 type hints stub file for the QtMultimediaWidgets module.
#
# Generated by SIP 4.18.1
#
# Copyright (c) 2016 Riverbank Computing Limited <info@riverbankcomputing.com>
# 
# This file is part of PyQt5.
# 
# This file may be used under the terms of the GNU General Public License
# version 3.0 as published by the Free Software Foundation and appearing in
# the file LICENSE included in the packaging of this file.  Please review the
# following information to ensure the GNU General Public License version 3.0
# requirements will be met: http://www.gnu.org/copyleft/gpl.html.
# 
# If you do not wish to use this file under the terms of the GPL version 3.0
# then you may purchase a commercial license.  For more information contact
# info@riverbankcomputing.com.
# 
# This file is provided AS IS with NO WARRANTY OF ANY KIND, INCLUDING THE
# WARRANTY OF DESIGN, MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.


import typing
import sip

from PyQt5 import QtWidgets
from PyQt5 import QtMultimedia
from PyQt5 import QtCore

# Support for QDate, QDateTime and QTime.
import datetime

# Convenient type aliases.
PYQT_SIGNAL = typing.Union[QtCore.pyqtSignal, QtCore.pyqtBoundSignal]
PYQT_SLOT = typing.Union[typing.Callable[..., None], QtCore.pyqtBoundSignal]

# Convenient aliases for complicated OpenGL types.
PYQT_OPENGL_ARRAY = typing.Union[typing.Sequence[int], typing.Sequence[float],
        sip.Buffer, None]
PYQT_OPENGL_BOUND_ARRAY = typing.Union[typing.Sequence[int],
        typing.Sequence[float], sip.Buffer, int, None]


class QVideoWidget(QtWidgets.QWidget, QtMultimedia.QMediaBindableInterface):

    def __init__(self, parent: typing.Optional[QtWidgets.QWidget] = ...) -> None: ...

    def setMediaObject(self, object: QtMultimedia.QMediaObject) -> bool: ...
    def paintEvent(self, event: QtGui.QPaintEvent) -> None: ...
    def moveEvent(self, event: QtGui.QMoveEvent) -> None: ...
    def resizeEvent(self, event: QtGui.QResizeEvent) -> None: ...
    def hideEvent(self, event: QtGui.QHideEvent) -> None: ...
    def showEvent(self, event: QtGui.QShowEvent) -> None: ...
    def event(self, event: QtCore.QEvent) -> bool: ...
    def saturationChanged(self, saturation: int) -> None: ...
    def hueChanged(self, hue: int) -> None: ...
    def contrastChanged(self, contrast: int) -> None: ...
    def brightnessChanged(self, brightness: int) -> None: ...
    def fullScreenChanged(self, fullScreen: bool) -> None: ...
    def setSaturation(self, saturation: int) -> None: ...
    def setHue(self, hue: int) -> None: ...
    def setContrast(self, contrast: int) -> None: ...
    def setBrightness(self, brightness: int) -> None: ...
    def setAspectRatioMode(self, mode: QtCore.Qt.AspectRatioMode) -> None: ...
    def setFullScreen(self, fullScreen: bool) -> None: ...
    def sizeHint(self) -> QtCore.QSize: ...
    def saturation(self) -> int: ...
    def hue(self) -> int: ...
    def contrast(self) -> int: ...
    def brightness(self) -> int: ...
    def aspectRatioMode(self) -> QtCore.Qt.AspectRatioMode: ...
    def mediaObject(self) -> QtMultimedia.QMediaObject: ...


class QCameraViewfinder(QVideoWidget):

    def __init__(self, parent: typing.Optional[QtWidgets.QWidget] = ...) -> None: ...

    def setMediaObject(self, object: QtMultimedia.QMediaObject) -> bool: ...
    def mediaObject(self) -> QtMultimedia.QMediaObject: ...


class QGraphicsVideoItem(QtWidgets.QGraphicsObject, QtMultimedia.QMediaBindableInterface):

    def __init__(self, parent: typing.Optional[QtWidgets.QGraphicsItem] = ...) -> None: ...

    def setMediaObject(self, object: QtMultimedia.QMediaObject) -> bool: ...
    def itemChange(self, change: QtWidgets.QGraphicsItem.GraphicsItemChange, value: typing.Any) -> typing.Any: ...
    def timerEvent(self, event: QtCore.QTimerEvent) -> None: ...
    def nativeSizeChanged(self, size: QtCore.QSizeF) -> None: ...
    def paint(self, painter: QtGui.QPainter, option: QtWidgets.QStyleOptionGraphicsItem, widget: typing.Optional[QtWidgets.QWidget] = ...) -> None: ...
    def boundingRect(self) -> QtCore.QRectF: ...
    def nativeSize(self) -> QtCore.QSizeF: ...
    def setSize(self, size: QtCore.QSizeF) -> None: ...
    def size(self) -> QtCore.QSizeF: ...
    def setOffset(self, offset: typing.Union[QtCore.QPointF, QtCore.QPoint]) -> None: ...
    def offset(self) -> QtCore.QPointF: ...
    def setAspectRatioMode(self, mode: QtCore.Qt.AspectRatioMode) -> None: ...
    def aspectRatioMode(self) -> QtCore.Qt.AspectRatioMode: ...
    def mediaObject(self) -> QtMultimedia.QMediaObject: ...
