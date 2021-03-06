U
    �`c_�'  �                   @   sT   d Z ddlZddlmZ ddlmZ G dd� dej�ZdZdZeee�Z	e	�
�  dS )	av  
Created by KingMak @ github.com/kingmak
GUI for Random Password Generator

Helpful Links
anchors        : https://www.tutorialspoint.com/python/tk_anchors.htm
place geometry : http://effbot.org/tkinterbook/place.htm
Labels         : https://www.tutorialspoint.com/python/tk_label.htm
Color Chart    : http://www.science.smith.edu/dftwiki/index.php/Color_Charts_for_TKinter
�    N)�
messagebox)�PasswordGeneratorc                       s6   e Zd Z� fdd�Zdd� Zd
dd�Zdd	� Z�  ZS )�Appc                    s"  t � ��  | �dd� | �d� | �d| �||� � | jdd� | jdd� | �d� | �	d	| j
� t� | _d
| _d| _d| _d�| j| j�}tj| ddd|dd�| _| jj| jd� | jjddtjd� tj| ddddtjd�| _| jj| jd� | jjddtjd� d}tj| ddd|dd�| _| jj| jd� | jjddtjd� tjdd�| _tj| dddd| jddtjdd�
| _| jj| jd� | jjddtjd� d}tj| ddd|dd�| _| jj| jd� | jjdd tjd� tjdd�| _ tj| dddd| j ddtjd!�	| _!| j!j| jd� | j!jdd tjd� d"}tj| ddd|dd�| _"| j"j| jd� | j"jdd#tjd� tjdd�| _#tj| dddd| j#ddtjd!�	| _$| j$j| jd� | j$jdd#tjd� d$}tj| ddd|dd�| _%| j%j| jd� | j%jdd%tjd� tjdd�| _&tj| dddd| j&ddtjd!�	| _'| j'j| jd� | j'jdd%tjd� tj(d&d'�}tj)| d(tj*|d| j
d)�| _+|| j+_,| j+jdd*tjd� tj| d+d(d,dtjtj*d-�| _-| j-j| jd� | j-jdd.tjd� d/}	tj| t.|	�dd|	dd�}
|
jd0d� |
jd1d2tjd� d S )3Nr   zRandom Password Generatorz%dx%d+%d+%dZblack)�bgZplus)Zcursorzimages/naruto.icoz<Return>)�Courier�   �bold�   �    zPassword Length ({} - {})�   Zgreen2�w)�width�fgr   �text�anchor)Zfontg{�G�z�?)ZrelxZrelyr   �   g333333�?)r   �bdr   r   �justifyg      �?zInclude Symbols (!@#$%^&*-_)g333333�?�   )�value�   )	r   r   r   �height�variable�onvalue�offvalue�reliefZhighlightcolorzInclude Numbers (0123456789)g)\���(�?)r   r   r   r   r   r   r   r   zInclude Lowercase (a - z)g���(\��?zInclude Uppercase (A - Z)g
ףp=
�?zimages/Sharingan.png)�file�   )r   r   �imager   Zcommandg      �?�'   Zcyan)r   r   r   r   r   r   g�������?zCreated by KingMak)r   �	   r   g      �?g�������?)/�super�__init__Z	resizable�titleZgeometry�GetAppCenterCoordsZ	configureZconfigZ
iconbitmapZbind�GenerateRandPassr   �passwordZ
widgetFont�minLen�maxLen�format�TkZLabelZ
passLenLblZplaceZNWZEntryZCENTER�passLenEntryZ
symbolsLblZIntVar�symbolChkBtnVarZCheckbuttonZFLATZsymbolChkBtnZ
numbersLbl�numbersChkBtnVarZnumbersChkBtnZlowercaseLbl�lowercaseChkBtnVarZlowercaseChkBtnZuppercaseLbl�uppercaseChkBtnVarZuppercaseChkBtnZ
PhotoImageZButtonZGROOVEZgenerateBtnr   �randPassEntry�len)�self�appWidth�	appHeight�passLenZsymbolsZnumbersZ	lowercaseZ	uppercaseZgenerateBtnImgZauthorZ	authorLbl��	__class__� �+C:\Users\KingMak\Desktop\Gui Pwd Gen\App.pyr"      s4   


������
��
��
���zApp.__init__c                 C   s4   | � � d |d  }| �� d |d  }||||fS )N�   )Zwinfo_screenwidthZwinfo_screenheight)r2   r   r   ZXcoordZYcoordr8   r8   r9   r$   �   s    zApp.GetAppCenterCoords� c                 C   s�   | j �� }|dkr*| j�| j| jd �}nbz>t|�}|| jk sH|| jkrf| �dd�| j| j�� W d S W n" t	k
r�   | �dd� Y d S X | j�
|| j�� | j�� | j�� | j�� �}| jjdt| j�� �d� | j�d|� d S )Nr;   r   ZErrorz+Password Length should be between {} and {}z$Password Length should be an integerr   )Zlast)r+   �getr&   ZRandIntr'   r(   �int�Popupr)   �	ExceptionZGenerater,   r-   r.   r/   r0   �deleter1   �insert)r2   Zeventr5   r&   r8   r8   r9   r%   �   s&    

�zApp.GenerateRandPassc                 C   s   t �||� d S )N)r   Z	showerror)r2   r#   �msgr8   r8   r9   r>   �   s    z	App.Popup)r;   )�__name__�
__module__�__qualname__r"   r$   r%   r>   �__classcell__r8   r8   r6   r9   r      s
    H
r   i:  i�  )�__doc__Ztkinterr*   r   �	Generatorr   r   r3   r4   ZappZmainloopr8   r8   r8   r9   �<module>   s    o
