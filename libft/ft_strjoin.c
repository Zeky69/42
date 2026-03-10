/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strjoin.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: zakburak <zakburak@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/30 00:00:00 by zakburak          #+#    #+#             */
/*   Updated: 2025/10/31 11:41:27 by zakburak         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_strjoin(char const *s1, char const *s2)
{
	char	*rst;
	int		size;

	if (!s1 || !s2)
		return (NULL);
	size = ft_strlen(s1) + ft_strlen(s2);
	rst = malloc(sizeof(char) * (size + 1));
	if (!rst)
		return (NULL);
	ft_memmove(rst, (char *)s1, ft_strlen(s1));
	ft_memmove(rst + ft_strlen(s1), (char *)s2, ft_strlen(s2));
	rst[size] = '\0';
	return (rst);
}
