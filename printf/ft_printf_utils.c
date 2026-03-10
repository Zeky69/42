/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf_utils.c                                  :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: zakburak <zakburak@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/10 12:59:24 by zakburak          #+#    #+#             */
/*   Updated: 2025/11/11 10:07:39 by zakburak         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

int	ft_putchar_fd(char c, int fd)
{
	if (write(fd, &c, 1) == -1)
		return (-1);
	return (1);
}

int	ft_putnbr_fd(int n, int fd)
{
	long	nb;
	int		count;
	int		ret;

	nb = n;
	count = 0;
	if (nb < 0)
	{
		if (ft_putchar_fd('-', fd) == -1)
			return (-1);
		nb = -nb;
		count += 1;
	}
	if (nb >= 10)
	{
		ret = ft_putnbr_fd((int)(nb / 10), fd);
		if (ret == -1)
			return (-1);
		count += ret;
	}
	if (ft_putchar_fd((char)(nb % 10 + '0'), fd) == -1)
		return (-1);
	return (count + 1);
}

int	ft_putunsigned_fd(unsigned int n, int fd)
{
	int	count;
	int	ret;

	count = 0;
	if (n >= 10)
	{
		ret = ft_putunsigned_fd(n / 10, fd);
		if (ret == -1)
			return (-1);
		count += ret;
	}
	ret = ft_putchar_fd((char)(n % 10 + '0'), fd);
	if (ret == -1)
		return (-1);
	return (count + ret);
}
