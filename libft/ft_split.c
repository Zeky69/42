/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_split.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: zakburak <zakburak@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/30 00:00:00 by zakburak          #+#    #+#             */
/*   Updated: 2025/11/07 14:56:19 by zakburak         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

static void	ft_free_split(char **words, int count)
{
	int	i;

	i = 0;
	while (i < count)
	{
		free(words[i]);
		i++;
	}
	free(words);
}

static char	*ft_word(char const *str, char sep, char **wrd)
{
	int	s;
	int	i;

	i = 0;
	s = 0;
	while (str[s] && !(str[s] == sep))
		s++;
	if (s == 0)
	{
		*wrd = NULL;
		return ((char *)str);
	}
	*wrd = (char *)malloc(sizeof(char) * (s + 1));
	if (!*wrd)
		return (NULL);
	(*wrd)[s] = '\0';
	while (i < s)
	{
		(*wrd)[i] = str[i];
		i++;
	}
	return ((char *)(str + s));
}

static char	*ft_ignore_sep(char const *str, char sep)
{
	while (*str && *str == sep)
		str++;
	return ((char *)str);
}

static int	ft_cword(char const *str, char sep)
{
	int	nb_word;
	int	in_word;
	int	i;

	nb_word = 0;
	in_word = 0;
	i = -1;
	while (str[++i] != '\0')
	{
		if (str[i] == sep)
		{
			in_word = 0;
		}
		else if (!in_word)
		{
			in_word = 1;
			nb_word++;
		}
	}
	return (nb_word);
}

char	**ft_split(char const *s, char c)
{
	char	*word;
	char	**words;
	int		i;

	if (!s)
		return (NULL);
	i = 0;
	words = (char **)malloc(sizeof(char *) * (ft_cword(s, c) + 1));
	if (!words)
		return (NULL);
	s = ft_ignore_sep(s, c);
	while (*s != '\0')
	{
		s = ft_word(s, c, &word);
		if (!s)
			return (ft_free_split(words, i), NULL);
		if (word)
			words[i++] = word;
		s = ft_ignore_sep(s, c);
	}
	words[i] = NULL;
	return (words);
}
