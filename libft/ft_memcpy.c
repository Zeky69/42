/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memcpy.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: zakburak <zakburak@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/28 12:29:35 by zakburak          #+#    #+#             */
/*   Updated: 2025/10/30 11:34:31 by zakburak         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	*ft_memcpy(void *dest, const void *src, size_t n)
{
	unsigned char	*tmp_d;
	unsigned char	*tmp_s;

	if (dest == (void *)0 && src == (void *)0)
		return (dest);
	tmp_d = (unsigned char *)dest;
	tmp_s = (unsigned char *)src;
	while (n-- > 0)
		*(tmp_d++) = *(tmp_s++);
	return (dest);
}
